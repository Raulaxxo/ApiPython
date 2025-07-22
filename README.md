# ApiPython

Proyecto base con estructura DevOps.
## ApiPython

API REST para gestión de tareas usando FastAPI y almacenamiento en JSON.

## Características
- CRUD de tareas (crear, leer, actualizar, eliminar)
- Endpoints documentados con OpenAPI
- Almacenamiento local en archivo JSON
- Listo para Docker y despliegue automatizado con GitHub Actions

## Estructura del proyecto
```
├── Docker-compose.yml
├── Dockerfile
├── Makefile
├── README.md
├── requirements.txt
├── docs/
├── infra/
│   └── terraform/
├── scripts/
├── src/
│   └── app/
│       ├── main.py
│       ├── models.py
│       ├── tareas.py
│       └── routes/
└── tests/
```

## Instalación local

1. Clona el repositorio:
   ```bash
   git clone https://github.com/<tu_usuario>/ApiPython.git
   cd ApiPython
   ```
2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la API:
   ```bash
   uvicorn src.app.main:app --reload
   ```

## Uso con Docker

1. Construye la imagen:
   ```bash
   docker build -t apipython .
   ```
2. Ejecuta el contenedor:
   ```bash
   docker run -p 8000:8000 apipython
   ```

## Endpoints principales
- `GET /tareas` - Lista todas las tareas
- `GET /tareas/{id}` - Obtiene una tarea por ID
- `POST /tareas` - Crea una nueva tarea
- `PUT /tareas/{id}` - Actualiza una tarea
- `DELETE /tareas/{id}` - Elimina una tarea

## Despliegue automático
El proyecto incluye un workflow de GitHub Actions para construir y subir la imagen Docker a Docker Hub en cada push a `main`.

## Pruebas
Coloca tus tests en la carpeta `tests/` y ejecútalos con:
```bash
python -m unittest discover -s tests
```

## Infraestructura
La carpeta `infra/terraform/` contiene archivos para desplegar recursos en la nube usando Terraform.

## Autor
- Raulaxxo
