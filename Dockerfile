# MCP Template Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# Entwicklungsabhängigkeiten (optional, für lokale Entwicklung)
# COPY requirements-dev.txt ./
# RUN pip install --no-cache-dir -r requirements-dev.txt


COPY app/ /app/


CMD ["python", "-u", "main.py"]
