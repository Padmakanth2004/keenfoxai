from llm.gemini_client import ask_gemini # for production
from llm.prompts import campaign_prompt
#from llm.mock_llm import ask_gemini
from utils.cache import get_cached_response, set_cached_response
import re


def extract_entities(intel):
    return [comp.lower() for comp in intel.keys()]


def validate_campaign_output(response, allowed_entities):
    if not response or len(response.strip()) == 0:
        return "No valid campaign generated."

    response_lower = response.lower()

    risky_words = ["maybe", "might", "possibly", "i think"]
    if any(word in response_lower for word in risky_words):
        return "Campaign output is uncertain based on available data."

    detected_entities = re.findall(r'\b[A-Z][a-zA-Z]+\b', response)

    for entity in detected_entities:
        if entity.lower() not in allowed_entities:
            return "Campaign contains information not present in intelligence data."

    return response


def generate_campaign(intel):
    if not intel or len(intel) == 0:
        return "No intelligence data available."

    valid_intel = {
        k: v for k, v in intel.items()
        if isinstance(v, dict) and "error" not in v
    }

    if not valid_intel:
        return "Not enough valid intelligence data to generate campaign."

    def has_meaningful_data(data):
        if isinstance(data, dict):
            return any(has_meaningful_data(v) for v in data.values())
        elif isinstance(data, list):
            return any(has_meaningful_data(v) for v in data)
        else:
            return data not in [None, "", "N/A"]

    if not has_meaningful_data(valid_intel):
        return "Not enough meaningful intelligence data to generate campaign."

    allowed_entities = extract_entities(valid_intel)

    prompt = campaign_prompt(valid_intel)

    prompt += """

STRICT RULES:
- Use ONLY the provided intelligence data
- Do NOT introduce new competitors
- Do NOT assume missing data
- If insufficient data, say: "Not enough data available"

RETURN STRICT FORMAT:
- Messaging
- Channels
- 3 Strategies with reasoning
"""

    # ✅ CACHE CHECK
    cached = get_cached_response(prompt)
    if cached:
        return cached

    try:
        response = ask_gemini(prompt)
    except Exception as e:
        return f"Error generating campaign: {e}"

    validated = validate_campaign_output(response, allowed_entities)

    if "not present in intelligence data" in validated.lower():
        return "Generated campaign could not be validated due to insufficient grounded data."

    # ✅ STORE CACHE
    set_cached_response(prompt, validated)

    return validated