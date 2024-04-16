
from openai import OpenAI
from dotenv import dotenv_values

# Load environment variables from .env file
config = dotenv_values(".env")

# Get the API key from the config dictionary
api_key = config.get("OPENAI_API_KEY")

# Set your OpenAI API key
OPENAI_APIKEY = api_key

# Initialize OpenAI client with the API key
client = OpenAI(api_key=OPENAI_APIKEY)

# Initialize messages list with a system message
MESSAGES = [
    {
        "role": "system",
        "content": "You are a Python Expert. You are asked to solve the python coding problems."
    }
]

def chat_with_gpt3(prompt):
    # Append user prompt to the messages list
    MESSAGES.append({'role': 'user', 'content': prompt})

    # Request chat completion from OpenAI
    chat_completion = client.chat.completions.create(
        messages=MESSAGES,
        model="text-davinci-003",  # Using GPT-3.5 model
    )

    # Append assistant response to the messages list
    assistant_response = chat_completion.choices[0].message.content
    MESSAGES.append({'role': 'assistant', 'content': assistant_response})

    return assistant_response

# Example usage
prompt = "How do I solve a Python coding problem?"
response = chat_with_gpt3(prompt)
print("Assistant:", response)
