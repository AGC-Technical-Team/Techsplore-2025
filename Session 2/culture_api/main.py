from fastapi import FastAPI
from routes import dishes

app = FastAPI()
app.include_router(dishes.router)
