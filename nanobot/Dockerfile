FROM python:3.12-slim
RUN pip install nanobot-ai
COPY . /app/nanobot/
WORKDIR /app/nanobot
CMD ["python", "entrypoint.py"]
