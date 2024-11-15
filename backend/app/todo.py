from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

import uuid

class Item(BaseModel):
    title: str
    description: str

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None



app = FastAPI()

todos = [
    {"id": uuid.uuid4(), "title": "Todo 1", "descripltion": "Desc of todo 1"}
]

@app.get("/todos")
def all_todos():
    return todos

@app.post("/add-todo")
async def new_todo(item: Item):

    newTodo = {
        "id": uuid.uuid4(),
        "title": item.title,
        "description": item.description
    }

    todos.append(newTodo)

    return {"message": "Successfully added new item"}

@app.patch("/update-todo/{id}")
async def update_todo():
    todos = todos.find(lambda: x => )

import uvicorn
uvicorn.run(app)