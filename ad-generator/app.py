import os
import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

print("Loading...\n")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a creative story for the following animal aimed at people adopting it:\n\nAnimal: Raccoon",
  temperature=0.5,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

result=response.choices[0].text
print(result)