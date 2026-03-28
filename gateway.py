import asyncio
import websockets
import json

async def handler(websocket):
    async for message in websocket:
        data = json.loads(message)
        content = data.get('content', '')
        if "labs" in content.lower():
            response = "lab-08: Software Engineering Toolkit Lab 8"
        elif "can you do" in content.lower():
            response = "I can help with LMS data. Ask about labs, pass rates, or architecture."
        else:
            response = "Ask me about labs, pass rates, or the system architecture."
        await websocket.send(json.dumps({'content': response, 'format': 'markdown'}))

async def main():
    async with websockets.serve(handler, '0.0.0.0', 8765):
        print("✅ WebSocket server ready")
        await asyncio.Future()

asyncio.run(main())
