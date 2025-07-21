# Imagen base de Python
FROM python:3.11-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY ./src/app ./src/app

# Exponer el puerto
EXPOSE 8000

# Comando para ejecutar la app
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

