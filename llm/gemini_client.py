from google import genai

client = genai.Client(api_key="AIzaSyAfAqYcTlDDf4SlXkwasM0kJR1tSd6AmUY")

def ask_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text