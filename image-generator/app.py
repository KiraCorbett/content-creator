import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

#user_prompt = input("Enter a prompt: ")

print("Loading...")

# response = openai.Image.create(
#   prompt="vintage raccoon listening to music",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']
# print(image_url)

response = openai.Image.create_variation(
  image=open("pyramid.png", "rb"),
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)