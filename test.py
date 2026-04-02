from google import genai

client = genai.Client(api_key="AIzaSyAgvs1H0yJvg4NYPov8m6sTONgmJdFxIB4")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello"
)

print(response.text)