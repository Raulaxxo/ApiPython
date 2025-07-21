from fastapi import FastAPI, HTTPException
from .models import ToDoModel
from .schemas import ToDo, ToDoCreate

app = FastAPI()
db = ToDoModel()

@app.get("/todos", response_model=list[ToDo])
def list_todos():
    return db.all()

@app.post("/todos", response_model=ToDo, status_code=201)
def create_todo(todo: ToDoCreate):
    return db.create(todo)

@app.get("/todos/{todo_id}", response_model=ToDo)
def get_todo(todo_id: int):
    todo = db.get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo no encontrado")
    return todo

@app.put("/todos/{todo_id}", response_model=ToDo)
def update_todo(todo_id: int, todo_data: ToDoCreate):
    todo = db.update(todo_id, todo_data)
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo no encontrado")
    return todo

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    todo = db.delete(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo no encontrado")
