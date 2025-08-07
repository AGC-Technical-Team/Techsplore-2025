# Simple Cultural Dishes API - Starter Version
# This is a single file to keep things SUPER simple for beginners!

from fastapi import FastAPI

# Create our FastAPI app (this is our "server")
app = FastAPI()

# Our simple data - just a list of dictionaries
dishes = [
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

# Route 1: Get all dishes
# When someone visits "/dishes", this function runs
@app.get("/dishes")
def get_all_dishes():
    return dishes

# Route 2: Get one specific dish
# When someone visits "/dishes/tabbouleh", this function runs
@app.get("/dishes/{dish_name}")
def get_one_dish(dish_name: str):
    # Look through all our dishes
    for dish in dishes:
        # If we find a match (ignoring uppercase/lowercase)
        if dish["name"].lower() == dish_name.lower():
            return dish
    
    # If we don't find the dish, return an error message
    return {"error": f"Sorry, we don't have {dish_name} in our menu!"}
