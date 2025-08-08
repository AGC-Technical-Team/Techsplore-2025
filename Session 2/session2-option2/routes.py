"""
API routes/endpoints
This file defines the API endpoints
"""

from fastapi import APIRouter
from models import MistralRequest, MistralResponse
from services import call_mistral_api

# Create a router for chat-related endpoints
chat_router = APIRouter()


@chat_router.post("/chat", response_model=MistralResponse)
def chat_with_mistral(request: MistralRequest):
    """
    Chat endpoint to interact with Mistral AI
    
    Args:
        request: MistralRequest containing api_key and ask_mistral_ai
    
    Returns:
        MistralResponse with the AI's reply or error information
    """
    
    # Call the service function to communicate with Mistral AI
    response = call_mistral_api(
        api_key=request.api_key,
        user_message=request.ask_mistral_ai
    )
    
    return response
