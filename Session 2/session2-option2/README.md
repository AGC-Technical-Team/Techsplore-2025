# Session 2 - Option 2: Mistral AI FastAPI Integration

This folder contains two versions of a FastAPI application that integrates with Mistral AI:

1. **Basic Version** (`main_basic.py`) - Everything in one file, perfect for beginners
2. **Modularized Version** - Organized into multiple files for better structure

## 📋 Prerequisites

- Python 3.7 or higher
- A Mistral AI API key (get one from https://console.mistral.ai/)

## 🚀 Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## 📁 Project Structure

### Basic Version (Single File)
- `main_basic.py` - All code in one file, easy to understand

### Modularized Version (Multiple Files)
- `main_modular.py` - Main application entry point
- `config.py` - Configuration settings
- `models.py` - Data models (request/response structures)
- `services.py` - Business logic for API calls
- `routes.py` - API endpoint definitions

## 🏃‍♂️ Running the Application

### Option 1: Run the Basic Version
```bash
uvicorn main_basic:app --reload
```

### Option 2: Run the Modularized Version
```bash
uvicorn main_modular:app --reload
```

The application will start on `http://localhost:8000`

## 📖 Using the API

### 1. Interactive Documentation
Visit `http://localhost:8000/docs` for Swagger UI documentation

### 2. Making a Request

**Endpoint:** `POST /chat`

**Request Body:**
```json
{
  "api_key": "your-mistral-api-key",
  "ask_mistral_ai": "Tell me about Japanese culture"
}
```

**Response:**
```json
{
  "response": "Japan has a rich and fascinating culture...",
  "status": "success"
}
```

### 3. Using curl
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "api_key": "your-api-key",
    "ask_mistral_ai": "What is French cuisine known for?"
  }'
```

## 🎓 For Beginners: Understanding the Code

### Why Two Versions?

1. **Basic Version** - Start here if you're new to FastAPI:
   - All code in one place
   - Easy to read from top to bottom
   - Good for learning and small projects

2. **Modularized Version** - Move here when you're comfortable:
   - Organized structure
   - Easier to maintain and scale
   - Follows professional best practices
   - Each file has a specific purpose

### Key Concepts Explained

#### FastAPI
- A modern web framework for building APIs with Python
- Automatically generates documentation
- Built-in data validation

#### Pydantic Models
- Define the structure of your data
- Automatic validation of incoming requests
- Type hints for better code clarity

#### API Integration
- How to make HTTP requests to external services
- Handling API keys securely
- Error handling for robust applications

### Learning Path

1. **Step 1:** Run the basic version and test it with the Swagger docs
2. **Step 2:** Read through `main_basic.py` to understand the flow
3. **Step 3:** Make a small modification (e.g., change the system prompt)
4. **Step 4:** Explore the modularized version to see how code can be organized
5. **Step 5:** Try adding a new endpoint or feature

## 🔒 Security Notes

- **Never commit API keys to version control**
- Consider using environment variables for API keys in production
- Add rate limiting for production deployments
- Validate and sanitize all user inputs

## 🐛 Troubleshooting

### Common Issues

1. **"Connection refused" error**
   - Make sure the server is running
   - Check if port 8000 is available

2. **"Unauthorized" from Mistral AI**
   - Verify your API key is correct
   - Check if your API key has credits

3. **"Module not found" error**
   - Install dependencies: `pip install -r requirements.txt`

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Mistral AI Documentation](https://docs.mistral.ai/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

## 💡 Exercises for Practice

1. **Easy:** Change the system prompt to make the AI a "helpful coding assistant"
2. **Medium:** Add a new endpoint that returns the conversation history
3. **Hard:** Implement streaming responses from Mistral AI
4. **Challenge:** Add user authentication to protect the API

## 🤝 Need Help?

- Check the FastAPI docs for framework questions
- Visit Mistral AI docs for API-specific issues
- Look at the error messages carefully - they often tell you what's wrong!

Happy coding! 🚀
