import os
from dotenv import load_dotenv
from groq import Groq
import groq

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
api_key = os.getenv("GROQ_API_KEY")

# Check if the API key was loaded successfully
if not api_key:
    raise ValueError("API key not found. Please check your .env file and ensure GROQ_API_KEY is set.")

# Initialize the Groq client
client = Groq(api_key=api_key)

def generate_content(prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-8b-instant"  # Model name should be a string
    )
    return response

# Example usage
if __name__ == "__main__":
    prompt = "Explain the importance of fast language models"
    try:
        result = generate_content(prompt)
        print(result)
    except groq.AuthenticationError as e:
        print(f"Authentication error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
