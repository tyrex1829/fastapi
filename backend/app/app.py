from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.get("/")
def home():
    return {"data": "Welcome to home page"}

@app.get("/contact")
def contact():
    return {"data": "Welcome to contact page"}

@app.post("/upload")
def handleImages(files: list[UploadFile]):
    print(files)
    return {"status": "got the file"}

import uvicorn
uvicorn.run(app)