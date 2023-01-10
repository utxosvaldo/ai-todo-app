import os
from pydoc import tempfilepager
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.Model.list())

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Give me the 5 names of the pillars of bitcoin",
    temperature=0.3,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

print(response)