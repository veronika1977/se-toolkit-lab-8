import asyncio
import websockets
import json

async def handler(websocket):
    async for message in websocket:
        data = json.loads(message)
        content = data.get('content', '')
        if "labs" in content.lower():
            response = "Lab 8: Software Engineering Toolkit Lab 8"
        else:
            response = "I can help with LMS data. Try asking about labs."
        await websocket.send(json.dumps({'content': response, 'format': 'markdown'}))

async def main():
    async with websockets.serve(handler, '0.0.0.0', 8765):
        print("✅ WebSocket server ready on port 8765")
        await asyncio.Future()

asyncio.run(main())
