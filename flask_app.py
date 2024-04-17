from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import dotenv_values

app = Flask(__name__)

# Load environment variables from .env file
config = dotenv_values(".env")

# Get the API key from the config dictionary
api_key = config.get("OPENAI_APIKEY")

# Set your OpenAI API key
OPENAI_APIKEY = api_key

# Initialize OpenAI client with the API key
client = OpenAI(api_key=OPENAI_APIKEY)

# Initialize messages list with a system message
MESSAGES = [
    {
        "role": "system",
        "content": "You are a Chef Expert. You are asked to give the recipis  of various dishes."
    }
]

def chat_with_gpt3(prompt):
    # Append user prompt to the messages list
    MESSAGES.append({'role': 'user', 'content': prompt})

    # Request chat completion from OpenAI
    chat_completion = client.chat.completions.create(
        messages=MESSAGES,
        model="gpt-3.5-turbo",  # Using GPT-3.5 model
    )

    # Append assistant response to the messages list
    assistant_response = chat_completion.choices[0].message.content
    MESSAGES.append({'role': 'assistant', 'content': assistant_response})

    return assistant_response

@app.route('/', methods=['POST'])
def home():
    # Get input data from the request
    data = request.json

    # Extract the message from the request data
    message = data.get("message")

    # Pass the message to the chat_with_gpt3 function
    response = chat_with_gpt3(message)

    # Construct the response in JSON format
    response_data = {"response": response}

    # Return the response in JSON format
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
