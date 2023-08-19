# Import required packages
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

# Load the .env file to read the api key
load_dotenv()

# Use the api key from the env file
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the language model
llm = OpenAI(openai_api_key=api_key)

# Predict a string
result = llm.predict("what is a hello world app?")
print(result)