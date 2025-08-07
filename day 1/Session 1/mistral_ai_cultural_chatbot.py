"""
MistralAI Cultural Chatbot
A simple chatbot that uses Mistral AI's API to answer cultural questions.
"""

# Import the requests library to make HTTP calls to the Mistral API
import requests

# Welcome message for users
print("Welcome to the Mistral Culture Chatbot!")
print("Type your question and press enter. Type 'exit' to quit.")

# Get the user's Mistral API key (this is like a password to access the AI service)
api_key = input("Enter your Mistral API key: ").strip()

# Choose which AI model to use - "mistral-tiny" is faster and cheaper
# "mistral-large-latest" is more powerful but requires higher access level
model = "mistral-tiny"  # or "mistral-large-latest" if you have access

# Main chat loop - keeps running until user types "exit"
while True:
    # Get user's question
    question = input("You: ")
    
    # Check if user wants to exit the program
    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Prepare the data to send to Mistral AI API
    # This follows the format that Mistral AI expects
    data = {
        "model": model,  # Which AI model to use
        "messages": [
            # System message: tells the AI how to behave
            {"role": "system", "content": "You are a friendly cultural assistant. You ONLY answer questions about culture, traditions, customs, festivals, food, art, music, languages, religions, and cultural practices from around the world. If someone asks about anything else (like math, science, technology, personal advice, etc.), politely remind them that you only discuss cultural topics and ask them to rephrase their question to be about culture."},
            # User message: the actual question from the user
            {"role": "user", "content": question}
        ]
    }
    
    # Set up headers for the API request
    # Authorization: proves we have permission to use the API
    # Content-Type: tells the server we're sending JSON data
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Send the request to Mistral AI's chat completion endpoint
    # This is where the magic happens - we send our question and get an AI response
    response = requests.post(
        "https://api.mistral.ai/v1/chat/completions",  # Mistral AI's API endpoint
        headers=headers,  # Authentication and content type
        json=data  # Our question and settings
    )
    
    # Parse the response from JSON format
    output = response.json()
    
    # Extract and print the AI's response
    # The response is nested in: choices[0].message.content
    print("Chatbot:", output["choices"][0]["message"]["content"])
