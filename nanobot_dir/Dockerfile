FROM python:3.12-slim-bookworm

RUN pip install nanobot-ai mcp

COPY nanobot /app/nanobot/
COPY mcp /app/mcp/

RUN pip install -e /app/mcp

CMD ["python", "/app/nanobot/entrypoint.py"]
