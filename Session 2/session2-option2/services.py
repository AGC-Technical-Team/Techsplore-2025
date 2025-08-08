"""
Service layer for Mistral AI integration
This file contains the business logic for communicating with Mistral AI
"""

import requests
from config import MISTRAL_API_URL, MISTRAL_MODEL, SYSTEM_PROMPT
from models import MistralResponse


def call_mistral_api(api_key: str, user_message: str) -> MistralResponse:
    """
    Make a request to the Mistral AI API
    
    Args:
        api_key: The Mistral AI API key
        user_message: The user's message/question
    
    Returns:
        MistralResponse object with the result
    """
    
    # Prepare the request data
    data = {
        "model": MISTRAL_MODEL,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    }
    
    # Set up headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        # Make the API request
        response = requests.post(MISTRAL_API_URL, headers=headers, json=data)
        response.raise_for_status()
        
        # Parse the response
        output = response.json()
        
        # Extract the AI's reply
        reply = output["choices"][0]["message"]["content"]
        
        return MistralResponse(
            response=reply,
            status="success"
        )
    
    except requests.exceptions.RequestException as e:
        # Handle request errors
        return MistralResponse(
            response=None,
            status="error",
            error_message=f"Error communicating with Mistral AI: {str(e)}"
        )
    
    except (KeyError, IndexError) as e:
        # Handle parsing errors
        return MistralResponse(
            response=None,
            status="error",
            error_message=f"Error parsing Mistral AI response: {str(e)}"
        )
