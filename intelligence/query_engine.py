#from llm.mock_llm import ask_gemini
from llm.gemini_client import ask_gemini  # for production
from utils.cache import get_cached_response, set_cached_response
import re

def clean_text(text):
    return re.sub(r'[^a-zA-Z0-9 ]', '', text.lower())


def retrieve_relevant_context(data, question, top_k=2):
    question_clean = clean_text(question)
    question_words = set(question_clean.split())

    scored_chunks = []

    for comp, details in data.items():
        text = clean_text(str(details) + " " + comp)
        words = set(text.split())

        score = len(question_words.intersection(words))

        if score > 0:
            scored_chunks.append((score, comp, details))

    scored_chunks.sort(reverse=True, key=lambda x: x[0])

    if not scored_chunks:
        return "No relevant data found.", []

    selected = scored_chunks[:top_k]

    context = "\n\n".join([f"{comp}: {details}" for _, comp, details in selected])

    # ✅ LIMIT CONTEXT SIZE (optimization)
    context = context[:1000]

    allowed_entities = [comp.lower() for _, comp, _ in selected]

    return context, allowed_entities


def validate_output(answer, context, allowed_entities):
    if not answer or len(answer.strip()) == 0:
        return "No valid response generated."

    answer_lower = answer.lower()

    risky_words = ["maybe", "might", "possibly", "i think"]
    if any(word in answer_lower for word in risky_words):
        return "The answer is uncertain based on available data."

    if context == "No relevant data found.":
        return "Not enough data available."

    detected_entities = re.findall(r'\b[A-Z][a-zA-Z]+\b', answer)

    for entity in detected_entities:
        if entity.lower() not in allowed_entities:
            return "Response contains information not present in retrieved context."

    return answer


def answer_query(data, question):
    if not question or len(question.strip()) == 0:
        return "Please ask a valid question."

    context, allowed_entities = retrieve_relevant_context(data, question)

    prompt = f"""
You are a competitive intelligence assistant.

STRICT RULES:
- Answer ONLY using the provided context
- Do NOT use external knowledge
- If answer not found, say: "Not enough data available"

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    # ✅ CACHE CHECK (IMPORTANT)
    cached = get_cached_response(prompt)
    if cached:
        return cached

    try:
        response = ask_gemini(prompt)
    except Exception as e:
        return f"Error generating response: {e}"

    validated = validate_output(response, context, allowed_entities)

    # ✅ STORE CACHE
    set_cached_response(prompt, validated)

    return validated