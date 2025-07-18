from fastapi import FastAPI
from app.routes import tareas

app = FastAPI(title="To-Do API - Raulaxxo")

app.include_router(tareas.router)
