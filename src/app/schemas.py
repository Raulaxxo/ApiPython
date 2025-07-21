from pydantic import BaseModel

class ToDoCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False

class ToDo(ToDoCreate):
    id: int
