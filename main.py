from google import genai

client = genai.Client(api_key="AIzaSyDRpy7nuaUNwfpsXf9JPoBvR0471-XcNZU")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="give me a random five letter word in lower case letters",
)
#variables
word = response.text 
GREEN = "\033[42m"
RESET = "\033[49m"
YELLOW = "\033[103m"


print ("give me a five letter word ")
guess = input ()

while len(guess) < 5: 
    guess += "_"
    
question = "Is "+guess+" a five letter word in the english dictionary? (respond yes if so or no if not)"
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=question,
).text.lower()

print (response)
