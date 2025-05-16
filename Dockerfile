# MCP Template Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY microagents/ ./microagents/

CMD ["python", "-u", "app/main.py"]
