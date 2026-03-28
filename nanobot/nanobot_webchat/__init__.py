from nanobot.channels.base import BaseChannel
import asyncio
import json
import websockets

class WebChatChannel(BaseChannel):
    def __init__(self, config):
        super().__init__(config)
        self.port = config.get('port', 8765)
        self.server = None
        
    async def start(self):
        self.server = await websockets.serve(self.handler, '0.0.0.0', self.port)
        self.logger.info(f"WebChat channel started on port {self.port}")
        
    async def handler(self, websocket, path):
        try:
            async for message in websocket:
                data = json.loads(message)
                response = await self.process_message(data.get('content', ''))
                await websocket.send(json.dumps({'content': response, 'format': 'markdown'}))
        except Exception as e:
            self.logger.error(f"Error: {e}")
            
    async def process_message(self, content):
        # Здесь будет вызов агента
        return f"Processing: {content}"
