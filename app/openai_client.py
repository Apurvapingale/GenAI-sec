import os
from groq import Groq
from config import GROQ_API_KEY

# Initialize the Groq client with the API key
client = Groq(api_key=GROQ_API_KEY)

def get_groq_response(question: str) -> str:
    """
    Get a response from Groq.
    """
    # Use Groq client to send the request and get the response
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
        model="llama3-8b-8192",  # Specify the model (can be adjusted)
    )

    # Return the answer from the response
    return chat_completion.choices[0].message.content.strip()
