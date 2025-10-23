from fastapi import FastAPI

app = FastAPI()

todos = []

@app.get("/")
def root():
    return {"message": "Todo App Running on AKS with GitOps"}

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def add_todo(item: dict):
    todos.append(item)
    return {"status": "added", "item": item}
