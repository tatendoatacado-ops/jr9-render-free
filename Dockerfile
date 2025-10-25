FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl build-essential \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=10000

# Corrigido o caminho do módulo para o Flask (main.py está dentro de "aplicativo")
CMD ["sh", "-c", "gunicorn -w 2 -b 0.0.0.0:${PORT:-10000} aplicativo.main:app"]
