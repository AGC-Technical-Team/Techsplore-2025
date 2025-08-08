"""
Basic FastAPI application for Mistral AI integration
This is a simple, beginner-friendly version that keeps everything in one file
"""

from fastapi import FastAPI
from pydantic import BaseModel
import requests

# Initialize the FastAPI application
app = FastAPI(title="Mistral AI Chat API", version="1.0.0")

# Mistral AI API endpoint
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"


# Define the request model using Pydantic
class MistralRequest(BaseModel):
    """Model for incoming chat requests"""
    api_key: str  # Your Mistral AI API key
    ask_mistral_ai: str  # The question or prompt for Mistral AI


# Root endpoint to check if the API is running
@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to the Mistral AI Chat API",
        "endpoints": {
            "/": "This welcome message",
            "/chat": "POST - Send a message to Mistral AI"
        }
    }


# Main chat endpoint
@app.post("/chat")
def chat_with_mistral(request: MistralRequest):
    """
    Send a message to Mistral AI and get a response
    
    Args:
        request: MistralRequest object containing api_key and ask_mistral_ai
    
    Returns:
        JSON response with the AI's reply
    """
    
    # Prepare the data for Mistral AI
    data = {
        "model": "mistral-small",  # Using the small model for cost efficiency
        "messages": [
            {
                "role": "system", 
                "content": "You are a friendly cultural assistant."
            },
            {
                "role": "user", 
                "content": request.ask_mistral_ai
            }
        ]
    }
    
    # Set up the headers with authentication
    headers = {
        "Authorization": f"Bearer {request.api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        # Make the request to Mistral AI
        response = requests.post(MISTRAL_API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse the response
        output = response.json()
        
        # Extract the AI's reply from the response
        reply = output["choices"][0]["message"]["content"]
        
        return {"response": reply, "status": "success"}
    
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return {
            "response": None,
            "status": "error",
            "error_message": f"Error communicating with Mistral AI: {str(e)}"
        }
    except (KeyError, IndexError) as e:
        # Handle parsing errors
        return {
            "response": None,
            "status": "error",
            "error_message": f"Error parsing Mistral AI response: {str(e)}"
        }


# Instructions for running the application
if __name__ == "__main__":
    print("""
    To run this application:
    1. Install dependencies: pip install fastapi uvicorn requests
    2. Run: uvicorn main_basic:app --reload
    3. Visit: http://localhost:8000/docs for interactive API documentation
    """)
