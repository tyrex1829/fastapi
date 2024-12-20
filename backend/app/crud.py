from fastapi import FastAPI
from enum import Enum

class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

# get method with "/" route, simple
@app.get("/home")
def home_route ():
    return {"Message": "Welcome to the home route of server"}

# get method on "/items" with {item_id} path-parameters -> async function
@app.get("/items/{item_id}")
async def get_item (item_id: int):
    return {"item_id": item_id}

# get async method on "/models" with {model_name} path-param with defined params in enum class
@app.get("/models/{model_name}")
async def get_models(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    if model_name is ModelName.resnet:
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuels"}

# get async method on "/query" with query-param -> name
@app.get("/query")
async def query_params(name: str):
    return {"message": f"Hello {name}"}

# 


import uvicorn
uvicorn.run(app)