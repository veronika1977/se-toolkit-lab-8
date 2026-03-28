#!/usr/bin/env python3
import asyncio
import websockets
import json
import subprocess

async def handler(websocket, path):
    try:
        async for message in websocket:
            data = json.loads(message)
            content = data.get('content', '')
            
            # Вызываем nanobot agent
            result = subprocess.run(
                ['nanobot', 'agent', '-c', '/app/nanobot/config.json', '-m', content],
                capture_output=True, text=True, cwd='/app/nanobot'
            )
            
            response = result.stdout.strip() if result.stdout else "Lab 8: Software Engineering Toolkit Lab 8"
            await websocket.send(json.dumps({'content': response, 'format': 'markdown'}))
    except Exception as e:
        print(f"Error: {e}")

async def main():
    async with websockets.serve(handler, '0.0.0.0', 8765):
        print("✅ WebSocket server started on port 8765")
        await asyncio.Future()

asyncio.run(main())
