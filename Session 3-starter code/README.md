# Session 3: FastAPI Starter - Your First API! 🚀

## What We're Building
A **super simple** web API that tells people about Lebanese dishes! 

Think of it like a digital menu that other programs can read.

## 🎯 Key Concepts (Simple!)

### What is a Server? 🖥️
A **server** is like a helpful robot that:
- Sits and waits for questions
- When someone asks a question, it gives an answer
- Never gets tired of answering the same questions

**Real example:** When you search on Google, Google's servers answer your question!

### What is an API? 📋
**API** = Application Programming Interface

Think of it like a **restaurant menu**:
- The menu shows what you can order
- It tells you exactly how to ask for each dish
- The kitchen (server) makes what you ordered

### What is a Route? 🛤️
A **route** is like a specific address that does something:
- `/dishes` = "Show me all the dishes!"
- `/dishes/tabbouleh` = "Tell me about tabbouleh!"

## 🏃‍♂️ Quick Start (3 Steps!)

### Step 1: Install FastAPI
```bash
pip install fastapi uvicorn
```

### Step 2: Start Your Server
```bash
uvicorn main:app --reload
```

### Step 3: Test It!
Open your web browser and try:
- **All dishes:** http://localhost:8000/dishes
- **One dish:** http://localhost:8000/dishes/tabbouleh
- **Magic docs:** http://localhost:8000/docs ← This is COOL!

## 🔍 Let's Look at the Code

Our entire API is just **ONE FILE** with **TWO FUNCTIONS**:

### The Data (Simple List)
```python
dishes = [
    {
        "name": "Tabbouleh", 
        "description": "A salad made with parsley, tomato, bulgur.", 
        "origin": "Lebanon"
    }
]
```

### Route 1: Get All Dishes
```python
@app.get("/dishes")
def get_all_dishes():
    return dishes
```
**What it does:** Someone asks for `/dishes`, we give them the whole list!

### Route 2: Get One Dish
```python
@app.get("/dishes/{dish_name}")
def get_one_dish(dish_name: str):
    # Look through our dishes and find the right one
```
**What it does:** Someone asks for `/dishes/tabbouleh`, we find just that dish!

## 🎮 Try These Examples

Once your server is running, try these in your browser:

1. **Get all dishes:**
   ```
   http://localhost:8000/dishes
   ```

2. **Get tabbouleh:**
   ```
   http://localhost:8000/dishes/tabbouleh
   ```

3. **Get fattoush:**
   ```
   http://localhost:8000/dishes/fattoush
   ```

4. **Try a dish that doesn't exist:**
   ```
   http://localhost:8000/dishes/pizza
   ```

## 🎨 Your Turn to Customize!

### Add Your Own Dish
Find this part in `main.py`:
```python
dishes = [
    # Add your dish here!
    {
        "name": "Your Dish Name", 
        "description": "What is it?", 
        "origin": "Where is it from?"
    }
]
```

### Try These Ideas:
- Add dishes from your country
- Change Lebanon to your culture
- Add more information like "spicy_level" or "cooking_time"

## 🤔 Common Questions

**Q: What's that `@app.get()` thing?**
A: It's called a "decorator" - it tells FastAPI "when someone visits this URL, run this function"

**Q: Why does it return dictionaries?**
A: FastAPI automatically converts Python dictionaries to JSON (the language of the web)

**Q: What's localhost:8000?**
A: Your computer's address! `localhost` = your computer, `8000` = the port number

## 🎪 Demo for Friends

1. **Start the server**: `uvicorn main:app --reload`
2. **Show the magic docs**: Go to http://localhost:8000/docs
3. **Try the "Try it out" buttons** - it's interactive!
4. **Change the code** while it's running - it updates automatically!

## 🚀 What's Next?

Once you understand this, you can:
- ✅ Build any kind of API (recipes, movies, games, etc.)
- ✅ Connect it to a real database
- ✅ Put it on the internet for everyone to use
- ✅ Add user accounts and security

## 🆘 Help! Something's Wrong?

### "Module not found"
```bash
pip install fastapi uvicorn
```

### "Port already in use"
```bash
uvicorn main:app --reload --port 8001
```

### Can't access localhost:8000
- Make sure the server is running
- Try http://127.0.0.1:8000 instead

---

**You just built your first API!** 🎉

**Next step:** Check out the "Session 3-final code" folder to see how pros organize their code!
