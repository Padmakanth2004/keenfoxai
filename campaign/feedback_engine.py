from llm.prompts import campaign_prompt
from llm.gemini_client import ask_gemini

def generate_campaign(intel):
    prompt = campaign_prompt(intel)
    return ask_gemini(prompt)