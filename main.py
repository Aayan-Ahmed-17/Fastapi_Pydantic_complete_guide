from fastapi import FastAPI

app = FastAPI()

#root get request
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

#hello get request
@app.get("/hello")
def say_hello():
    return {"message": "Hello, FastAPI!"}

#path parameter get request
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

