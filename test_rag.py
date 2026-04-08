from intelligence.query_engine import (
    retrieve_relevant_context,
    answer_query,
    validate_output
)

# ✅ Step 4: Local test data (RAG testing)
data = {
    "Notion": {"pricing": "free and paid plans", "features": "notes, docs"},
    "Asana": {"pricing": "premium plans", "features": "task tracking"}
}

# -------------------------------
# 🔹 1. TEST RETRIEVAL (RAG)
# -------------------------------
context, allowed_entities = retrieve_relevant_context(
    data, "pricing of Notion"
)

print("\n===== RETRIEVED CONTEXT =====\n")
print(context)

print("\nAllowed Entities:", allowed_entities)


# -------------------------------
# 🔹 2. TEST FULL PIPELINE
# -------------------------------
print("\n===== FULL RESPONSE TEST =====\n")

response = answer_query(data, "What is the pricing of Notion?")
print(response)


# -------------------------------
# 🔹 3. TEST VALIDATION LOGIC
# -------------------------------
print("\n===== VALIDATION TEST =====\n")

fake_response = "I think Notion might be better"

print(
    "Hallucination Test:",
    validate_output(fake_response, context, allowed_entities)
)

print(
    "Empty Test:",
    validate_output("", context, allowed_entities)
)

print(
    "No Context Test:",
    validate_output("Notion is great", "No relevant data found.", [])
)