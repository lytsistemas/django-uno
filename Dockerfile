# Usar una imagen oficial de Python como base
FROM python:3.10-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar los archivos de tu aplicación en el contenedor
COPY . /app/

# Instalar las dependencias necesarias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer el puerto que Django usará (por defecto 8000)
EXPOSE 8000

# Establecer el comando por defecto para iniciar el servidor de desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

