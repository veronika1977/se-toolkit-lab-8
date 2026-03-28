import asyncio
import websockets
import json

async def handler(websocket):
    async for message in websocket:
        data = json.loads(message)
        content = data.get('content', '')
        if "labs" in content.lower():
            response = "lab-08"
        else:
            response = "Ask about labs"
        await websocket.send(json.dumps({'content': response}))

async def main():
    async with websockets.serve(handler, '0.0.0.0', 8765):
        print("✅ WebSocket server ready")
        await asyncio.Future()

asyncio.run(main())
