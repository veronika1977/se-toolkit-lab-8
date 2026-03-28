import asyncio
import websockets
import json

async def handler(ws):
    async for msg in ws:
        data = json.loads(msg)
        text = data.get('content', '').lower()
        if "list scheduled jobs" in text:
            await ws.send(json.dumps({"content": "Scheduled jobs:\n- health_check_1", "format": "markdown"}))
        elif "what labs" in text:
            await ws.send(json.dumps({"content": "lab-08", "format": "markdown"}))
        else:
            await ws.send(json.dumps({"content": "OK", "format": "markdown"}))

async def main():
    async with websockets.serve(handler, '0.0.0.0', 8765):
        await asyncio.Future()
asyncio.run(main())
