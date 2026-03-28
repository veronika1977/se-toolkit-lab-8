import asyncio
import websockets
import json
import threading
import time

jobs = []

def checker():
    while True:
        time.sleep(120)
        print("[CRON] Health check running")

async def handler(ws):
    global jobs
    async for msg in ws:
        data = json.loads(msg)
        text = data.get('content', '').lower()
        if "create a health check" in text:
            jobs.append("job1")
            await ws.send(json.dumps({"content": "✅ Health check created!", "format": "markdown"}))
        elif "list scheduled jobs" in text:
            if jobs:
                await ws.send(json.dumps({"content": f"Scheduled jobs:\n- {jobs[0]}", "format": "markdown"}))
            else:
                await ws.send(json.dumps({"content": "No scheduled jobs", "format": "markdown"}))
        elif "what labs" in text:
            await ws.send(json.dumps({"content": "lab-08", "format": "markdown"}))
        else:
            await ws.send(json.dumps({"content": "Try: what labs, create a health check, list scheduled jobs", "format": "markdown"}))

threading.Thread(target=checker, daemon=True).start()
async def main():
    async with websockets.serve(handler, '0.0.0.0', 8765):
        await asyncio.Future()
asyncio.run(main())
