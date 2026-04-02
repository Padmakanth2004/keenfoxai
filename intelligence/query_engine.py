from llm.gemini_client import ask_gemini

def answer_query(data, question):
    prompt = f"""
You are a competitive intelligence assistant.

Answer the question using ONLY the provided competitor data.

STRICT INSTRUCTIONS:
- Do NOT use external knowledge
- Do NOT hallucinate
- If data is missing, say: "Not enough data available"

FORMAT YOUR ANSWER CLEARLY:
1. Start with a short summary (1–2 lines)
2. Then provide bullet points
3. Keep it simple and easy to read
4. Mention competitor names where relevant

---

COMPETITOR DATA:
{data}

---

QUESTION:
{question}

---

Answer:
"""
    return ask_gemini(prompt)