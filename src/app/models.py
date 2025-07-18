from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: Optional[str] = None
    completado: bool = False
    fecha_creacion: datetime = datetime.now()
