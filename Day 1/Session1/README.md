# MistralAI Cultural Chatbot

Welcome to your first AI chatbot project! This simple Python program connects to Mistral AI's powerful language model to answer questions about culture, traditions, and customs from around the world.

**Important**: This chatbot is designed to ONLY discuss cultural topics. It will politely decline to answer questions about other subjects like math, science, technology, or personal advice.

## What is an API?

**API** stands for **Application Programming Interface**. Think of it like a waiter at a restaurant:

- **You (the customer)** = Your Python program
- **The waiter** = The API
- **The kitchen** = Mistral AI's servers and AI models

Just like you tell the waiter what you want to eat, your program tells the API what you want the AI to do. The waiter takes your request to the kitchen, and brings back your food - similarly, the API takes your question to the AI and brings back the answer.

### Why do we need APIs?

- **Easy Communication**: APIs provide a standard way for different software to talk to each other
- **No Complex Setup**: You don't need to download and run huge AI models on your computer
- **Always Updated**: The AI company maintains and improves their models
- **Scalable**: Can handle requests from millions of users

## How This System Works

### 1. **Authentication (API Key)**
```python
api_key = input("Enter your Mistral API key: ").strip()
```
- Your API key is like a membership card that proves you're allowed to use the service
- It also tracks your usage for billing purposes
- Never share your API key publicly!

### 2. **Request Structure**
```python
data = {
    "model": model,
    "messages": [
        {"role": "system", "content": "You are a friendly cultural assistant."},
        {"role": "user", "content": question}
    ]
}
```
- **model**: Which AI brain to use (mistral-tiny vs mistral-large-latest)
- **system message**: Sets the AI's personality and behavior
- **user message**: Your actual question

### 3. **HTTP Request**
```python
response = requests.post(
    "https://api.mistral.ai/v1/chat/completions",
    headers=headers,
    json=data
)
```
- Uses the `requests` library to send data over the internet
- **POST**: Sending data to the server (vs GET which just asks for data)
- **Headers**: Include authentication and specify data format
- **JSON**: A standard format for sending structured data

### 4. **Response Parsing**
```python
output = response.json()
print("Chatbot:", output["choices"][0]["message"]["content"])
```
- The API returns structured data containing the AI's response
- We extract just the text content to display to the user

## Prerequisites

1. **Python 3.6+** installed on your computer
2. **requests library**:
   ```bash
   pip install requests
   ```
3. **Mistral AI API key** (get one from [mistral.ai](https://mistral.ai))

## How to Run

1. Open terminal/command prompt
2. Navigate to this folder:
   ```bash
   cd "Day 1/Session1"
   ```
3. Run the program:
   ```bash
   python mistral_ai_cultural_chatbot.py
   ```
4. Enter your API key when prompted
5. Start asking cultural questions!

## Example Conversation

```
Welcome to the Mistral Culture Chatbot!
Type your question and press enter. Type 'exit' to quit.
Enter your Mistral API key: your_api_key_here

You: What are some traditional foods in Japan?
Chatbot: Japan has many traditional foods! Some popular ones include sushi (raw fish with rice), ramen (noodle soup), tempura (battered and fried vegetables or seafood), and miso soup. Traditional Japanese meals often include rice, miso soup, pickled vegetables, and grilled fish.

You: Tell me about Diwali celebrations
Chatbot: Diwali, also known as the Festival of Lights, is one of the most important Hindu festivals...

You: exit
Goodbye!
```

## Key Concepts for Beginners

### **API Endpoints**
Think of these as specific addresses for different services:
- `https://api.mistral.ai/v1/chat/completions` = "Please have a conversation with me"
- Different endpoints do different things (chat, text completion, etc.)

### **HTTP Methods**
- **GET**: "Give me information" (like visiting a webpage)
- **POST**: "Here's some data, do something with it" (like submitting a form)

### **JSON (JavaScript Object Notation)**
A way to structure data that both humans and computers can easily read:
```json
{
    "name": "John",
    "age": 25,
    "hobbies": ["reading", "coding"]
}
```

### **Headers**
Extra information sent with your request:
- `Authorization`: Proves who you are
- `Content-Type`: Tells the server what kind of data you're sending

## Troubleshooting

### Common Issues:

1. **"Invalid API Key"**
   - Double-check your API key is correct
   - Make sure you have credits in your Mistral account

2. **"requests module not found"**
   - Install it with: `pip install requests`

3. **Connection errors**
   - Check your internet connection
   - Verify the API endpoint URL is correct

4. **Rate limiting errors**
   - You're sending requests too quickly
   - Wait a moment between requests

## Next Steps

Once you understand this basic chatbot, you can:
- Modify the system message to create different personalities
- Add conversation history to maintain context
- Implement different AI models for various use cases
- Add error handling for better user experience
- Create a web interface instead of command line

## Learning Resources

- [Mistral AI Documentation](https://docs.mistral.ai/)
- [Python Requests Library](https://requests.readthedocs.io/)
- [What are APIs? (Beginner Guide)](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)

---

**Happy Coding!** 🎉

Remember: The best way to learn programming is by experimenting. Try modifying the code and see what happens!
