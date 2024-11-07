# Imagen base
FROM python:3.12-slim

# Configurar el directorio de trabajo
WORKDIR /app

# Instalar las dependencias necesarias para mysqlclient
RUN apt-get update && \
    apt-get install -y gcc pkg-config libmariadb-dev && \
    rm -rf /var/lib/apt/lists/*

# Copiar requirements.txt y otros archivos necesarios
COPY requirements.txt /app/requirements.txt

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . /app

# Exponer el puerto 8000 para Django
EXPOSE 8000

# Comando para iniciar el servidor de desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
