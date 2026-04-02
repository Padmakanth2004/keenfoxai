from llm.prompts import competitor_prompt
from llm.gemini_client import ask_gemini
import json
import re

def extract_signals(data):
    prompt = competitor_prompt(data)
    response = ask_gemini(prompt)

    try:
        # Extract JSON safely
        match = re.search(r'\{.*\}', response, re.DOTALL)
        if match:
            return json.loads(match.group())
        else:
            raise ValueError("No JSON found")

    except:
        # ✅ ALWAYS return valid structure (CRITICAL)
        return {
            "feature_launches": [],
            "messaging_shifts": [],
            "customer_sentiment": {
                "loves": [],
                "complaints": []
            },
            "pricing_changes": [],
            "gaps": []
        }