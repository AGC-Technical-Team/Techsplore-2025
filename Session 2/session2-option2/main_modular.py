"""
Modularized FastAPI application for Mistral AI integration
Main application file that brings everything together
"""

from fastapi import FastAPI
from routes import chat_router
from config import APP_TITLE, APP_VERSION

# Initialize the FastAPI application
app = FastAPI(title=APP_TITLE, version=APP_VERSION)

# Include the chat router
app.include_router(chat_router)


# Root endpoint
@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {
        "message": f"Welcome to {APP_TITLE}",
        "version": APP_VERSION,
        "endpoints": {
            "/": "This welcome message",
            "/chat": "POST - Send a message to Mistral AI",
            "/docs": "Interactive API documentation"
        }
    }


if __name__ == "__main__":
    print("""
    To run this application:
    1. Install dependencies: pip install fastapi uvicorn requests python-dotenv
    2. Run: uvicorn main_modular:app --reload
    3. Visit: http://localhost:8000/docs for interactive API documentation
    """)
