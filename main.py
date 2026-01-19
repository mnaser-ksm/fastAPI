from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

db: Dict[int, dict] = {}
next_id = 1
items = ["item1", "item2", "item3"]
class UserCreate(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/items")
def get_items():
    return items
@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/test")
def test():
    return {"test": "this is a test endpoint"}

@app.get("/greet")
def greet(name: str ="mohammed"):
    return {"greeting": f"Hello, {name}!"}

@app.get("/index/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/users/test")
def create_user(user: UserCreate):
    return {"created": user}

@app.post("/users")
def create_user(user: UserCreate):
    global next_id
    user_id = next_id
    next_id += 1
    db[user_id] = user.model_dump()
    return {"id": user_id, "user": db[user_id]}

@app.get("/allusers")
def list_users():
    return db.items()