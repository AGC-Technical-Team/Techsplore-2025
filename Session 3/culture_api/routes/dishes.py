from fastapi import APIRouter
from models.dish import Dish

router = APIRouter()

# Dummy data
dishes = [
    Dish(name="Tabbouleh", description="A salad made with parsley, tomato, bulgur.", origin="Lebanon"),
    Dish(name="Fattoush", description="A salad with crispy bread and fresh veggies.", origin="Levant")
]

@router.get("/dishes")
def get_dishes():
    return dishes

@router.get("/dishes/{name}")
def get_dish(name: str):
    for dish in dishes:
        if dish.name.lower() == name.lower():
            return dish
    return {"error": "Dish not found"}
