# Session 3: FastAPI Cultural Dishes API

## 🎯 Key Concepts (Simple Definitions)

### What is a Server?
A **server** is just a computer (or program) that listens for requests from other computers (clients), and sends back responses.

**Example:** Google's servers send you search results when you type a query.

### What is an API?
**API** = Application Programming Interface

It's like a **menu in a restaurant**: it tells you what you can ask for, and how to ask for it.

In web development, an API lets programs talk to each other over the internet.

### What is a Route?
A **route** is a specific URL on your server that does something.

**Examples:**
- `/dishes` could show all dishes
- `/dishes/tabbouleh` could show details about tabbouleh
- Each route is connected to a function in your code

## 🏗️ Project Structure
```
culture_api/
│
├── main.py              # Entry point (runs the server)
├── routes/
│    └── dishes.py       # All dish-related endpoints
├── models/
│    └── dish.py         # Data structure for a Dish
├── requirements.txt     # Dependencies
├── .gitignore          # Files to ignore in git
└── .github/
     └── workflows/
         └── ci.yml      # GitHub Actions for simple CI
```

## 🚀 How to Run

### 1. Install Dependencies
```bash
cd "Session 3/culture_api"
pip install -r requirements.txt
```

### 2. Start the Server
```bash
uvicorn main:app --reload
```

### 3. Test the API
Open your browser and visit:
- **All dishes:** http://localhost:8000/dishes
- **Specific dish:** http://localhost:8000/dishes/tabbouleh
- **Interactive docs:** http://localhost:8000/docs

## 📱 API Endpoints

### GET `/dishes`
Returns all traditional dishes in our database.

**Response:**
```json
[
  {
    "name": "Tabbouleh",
    "description": "A salad made with parsley, tomato, bulgur.",
    "origin": "Lebanon"
  },
  {
    "name": "Fattoush",
    "description": "A salad with crispy bread and fresh veggies.",
    "origin": "Levant"
  }
]
```

### GET `/dishes/{name}`
Returns details about a specific dish.

**Example:** `/dishes/tabbouleh`

**Response:**
```json
{
  "name": "Tabbouleh",
  "description": "A salad made with parsley, tomato, bulgur.",
  "origin": "Lebanon"
}
```

## 🔧 Code Explanation

### Server (main.py)
The FastAPI app is your **server**, running locally at `localhost:8000`.

### API (routes/dishes.py)
Your app's endpoints (like `/dishes`) are **APIs** for getting data about cultural dishes.

### Routes
`/dishes` and `/dishes/{name}` are the **routes** or **URLs** handled by your code.

### Clean Code
Code is split into files by purpose:
- **models/**: Data structures
- **routes/**: API endpoints
- **main.py**: App entry point

### DevOps/CI (.github/workflows/ci.yml)
The `.yml` file runs a check every time you push code, teaching basic CI/CD.

## 🎪 Demo Steps

1. **Run the app locally:**
   ```bash
   uvicorn main:app --reload
   ```

2. **Open interactive docs:**
   Visit http://localhost:8000/docs and show the interactive API documentation

3. **Push to GitHub:**
   Show the CI workflow passing automatically

## 🎨 Customization Ideas

Want to add your own culture? Easy! Just modify `routes/dishes.py`:

```python
dishes = [
    Dish(name="Pad Thai", description="Stir-fried rice noodles with shrimp.", origin="Thailand"),
    Dish(name="Tacos", description="Corn tortillas with various fillings.", origin="Mexico"),
    # Add your dishes here!
]
```

## 🤖 What is CI/CD?

**CI** = Continuous Integration
- Automatically checks your code when you push to GitHub
- Catches errors early

**CD** = Continuous Deployment
- Could automatically deploy your app (we're keeping it simple for now)

Our CI workflow:
1. Runs when you push code
2. Sets up Python
3. Installs dependencies
4. Checks code quality with flake8

## 🎓 Learning Outcomes

After this session, you'll understand:
- ✅ How to build a REST API
- ✅ What servers, APIs, and routes are
- ✅ How to organize code cleanly
- ✅ Basic DevOps with GitHub Actions
- ✅ How to document and test APIs

## 🚀 Next Steps

1. Add more dishes from different cultures
2. Add POST endpoints to create new dishes
3. Connect to a real database
4. Deploy to the cloud
5. Add authentication

---

**Happy API Building!** 🎉
