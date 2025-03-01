from google import genai
import random

client = genai.Client(api_key="AIzaSyDRpy7nuaUNwfpsXf9JPoBvR0471-XcNZU")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="give me just a list of 20 random five letter words with no explanation or punctuation."
)
 
wordList = response.text.splitlines()
word = random.choice(wordList)
 
#variables
GREEN = "\033[42m"
RESET = "\033[49m"
YELLOW = "\033[103m"

for i in range(5):
    while True:
        print ("give me a five letter word ")
        guess = input ()[0:5]

        while len(guess) < 5: 
            guess += "!"
        
        question = "Is "+guess+" a five letter word in the Miriam-Webster English Dictionary? (yes or no)"
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=question,
        ).text.lower()

        if "yes" in response:
            break

    result = ""
    for i in range(5):
        letter = guess[i]
        if word[i] == letter:
            result += GREEN + letter + RESET
        elif letter in word:
            result += YELLOW + letter + RESET 
        else: 
            result += letter 
    print(result)