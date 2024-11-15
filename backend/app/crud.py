from fastapi import FastAPI

app = FastAPI()

# get method with "/" route, simple
@app.get("/home")
def home_route ():
    return {"Message": "Welcome to the home route of server"}

import uvicorn
uvicorn.run(app)