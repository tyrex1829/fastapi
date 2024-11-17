from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

class Item(BaseModel):
    title: str
    description: str

class TodoUpdate(BaseModel):
    updatedTitle: Optional[str] = None
    updatedDescription: Optional[str] = None


app = FastAPI()

todos = [
    {"id": str(uuid.uuid4()), "title": "Todo 1", "description": "Desc of todo 1"}
]

@app.get("/todos")
def all_todos():
    return todos

@app.post("/add-todo")
async def new_todo(item: Item):

    newTodo = {
        "id": str(uuid.uuid4()),
        "title": item.title,
        "description": item.description
    }
    print(newTodo)
    todos.append(newTodo)

    return {"message": "Successfully added new item", "todo": newTodo}

@app.patch("/update-todo/{id}")
async def update_todo(id: str, todo_update: TodoUpdate):
    for todo in todos:
        if todo["id"] == id:
            if todo_update.updatedTitle is not None:
                todo["title"] = todo_update.updatedTitle
            if todo_update.updatedDescription is not None:
                todo["description"] = todo_update.updatedDescription
            return {"message": "Todo updated successfully!", "todo": todo}
    
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/delete-todo")
async def delete_todo(id: str):
    for idx, todo in enumerate(todos):
        if todo["id"] == id:
            deleted_todo = todos.pop(idx)
            return {"message": "Todo Deleted Successfully", "todo": deleted_todo}
        
    raise HTTPException(status_code=404, detail="todo not found")

import uvicorn
uvicorn.run(app)