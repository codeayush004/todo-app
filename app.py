from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
todos = []


@app.get("/")
def root():
    return {"message": "Todo App API is running"}

@app.get("/todos")
def get_todos():
    return {"todos": todos}

@app.post("/todos")
def add_todo(item: dict):
    todos.append(item)
    return {"status": "added", "item": item}


instrumentator = Instrumentator().instrument(app)
instrumentator.expose(app, endpoint="/metrics")
