"""
Data models for the API
This file defines the structure of requests and responses
"""

from pydantic import BaseModel
from typing import Optional


class MistralRequest(BaseModel):
    """
    Model for incoming chat requests
    
    Attributes:
        api_key: Your Mistral AI API key
        ask_mistral_ai: The question or prompt for Mistral AI
    """
    api_key: str
    ask_mistral_ai: str


class MistralResponse(BaseModel):
    """
    Model for chat responses
    
    Attributes:
        response: The AI's response text (None if error)
        status: Either 'success' or 'error'
        error_message: Error details if status is 'error'
    """
    response: Optional[str]
    status: str
    error_message: Optional[str] = None
