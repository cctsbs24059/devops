FROM python:3.13-slim

# LABEL org.opencontainers.image.source=https://github.com/cctsbs24059/devops

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y netcat-traditional && \
    pip install -r requirements.txt && \
    rm -rf /var/lib/apt/lists

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]

