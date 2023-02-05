import os
import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
#print(os.getenv("OPENAI_API_KEY"))
#openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)

result=response.choices[0].text
print(result)