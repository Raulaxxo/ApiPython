from fastapi import APIRouter, HTTPException
from app.models import Tarea
from typing import List
import json, os

router = APIRouter()

STORAGE_FILE = "app/storage.json"

def leer_tareas():
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r") as f:
        return json.load(f)

def guardar_tareas(tareas):
    with open(STORAGE_FILE, "w") as f:
        json.dump(tareas, f, default=str, indent=4)

@router.get("/tareas", response_model=List[Tarea])
def obtener_tareas():
    return leer_tareas()

@router.get("/tareas/{tarea_id}", response_model=Tarea)
def obtener_tarea(tarea_id: int):
    tareas = leer_tareas()
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@router.post("/tareas", response_model=Tarea)
def crear_tarea(tarea: Tarea):
    tareas = leer_tareas()
    tarea.id = len(tareas) + 1
    tareas.append(tarea.dict())
    guardar_tareas(tareas)
    return tarea

@router.put("/tareas/{tarea_id}", response_model=Tarea)
def actualizar_tarea(tarea_id: int, datos: Tarea):
    tareas = leer_tareas()
    for i, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            tareas[i] = datos.dict()
            guardar_tareas(tareas)
            return datos
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@router.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int):
    tareas = leer_tareas()
    nuevas = [t for t in tareas if t["id"] != tarea_id]
    guardar_tareas(nuevas)
    return {"mensaje": "Tarea eliminada"}
