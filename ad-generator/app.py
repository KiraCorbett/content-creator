import os
import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

user_prompt = input("Enter a prompt: ")
#user_temp = input("Enter a temperature (0 low risk, 0.9 AI will take risks): ")

# prompt="Write a creative ad for the following product to run on Facebook aimed at parents:\n\nProduct: Learning Room is a virtual environment to help students from kindergarten to high school excel in school."

print("Loading...")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=user_prompt,
  temperature=0.5,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

result=response.choices[0].text
print(result)