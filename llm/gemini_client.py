from google import genai

client = genai.Client(api_key="apikey here")  # replace with your actual API key

def ask_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text