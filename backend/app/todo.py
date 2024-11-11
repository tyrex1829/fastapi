from fastapi import FastAPI
import uuid

app = FastAPI()

todos = [
    {"id": uuid.uuid4(), "title": "Todo 1", "descripltion": "Desc of todo 1"}
]

@app.get("/todos")
def allTodos():
    return todos

@app.post("new-todo")
def newTodo():
    {id, title, description} = 