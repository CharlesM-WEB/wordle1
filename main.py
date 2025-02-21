from google import genai

client = genai.Client(api_key="AIzaSyDRpy7nuaUNwfpsXf9JPoBvR0471-XcNZU")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="give me a random five letter word in lower case letters",
)


word = response.text 
