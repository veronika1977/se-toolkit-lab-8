FROM python:3.14-slim-bookworm

RUN pip install nanobot-ai mcp

# Копируем всё из текущей директории
COPY . /app/nanobot/
COPY ../mcp /app/mcp/

# Устанавливаем зависимости
RUN pip install -e /app/mcp
RUN pip install -e /app/nanobot/nanobot-channel-protocol
RUN pip install -e /app/nanobot/nanobot-webchat

CMD ["python", "/app/nanobot/entrypoint.py"]
