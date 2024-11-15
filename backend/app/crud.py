from fastapi import FastAPI

app = FastAPI()

# get method with "/" route, simple
@app.get("/home")
def home_route ():
    return {"Message": "Welcome to the home route of server"}

# get method on "/items" with {item_id} path-parameters -> async function
@app.get("/items/{item_id}")
async def get_item (item_id: int):
    return {"item_id": item_id}

import uvicorn
uvicorn.run(app)