import json
import sys
import asyncio
from http.server import HTTPServer, BaseHTTPRequestHandler

# Добавляем путь к MCP
sys.path.insert(0, '/root/se-toolkit-lab-8')
sys.path.insert(0, '/root/se-toolkit-lab-8/mcp')

from mcp_lms.server import call_tool
import mcp_lms.server

# Устанавливаем URL для MCP
mcp_lms.server._base_url = 'http://localhost:42001'

class SmartLLMHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/v1/chat/completions':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)
            
            messages = data.get('messages', [])
            last_message = messages[-1]['content'] if messages else ""
            
            # Вызываем MCP инструмент для запросов о лабораториях
            if "labs" in last_message.lower():
                result = asyncio.run(call_tool('lms_labs', {}))
                content = result[0].text
            elif "scores" in last_message.lower():
                content = "Please specify which lab you want to see scores for. Available labs: Lab 8"
            elif "pass rate" in last_message.lower():
                result = asyncio.run(call_tool('lms_pass_rates', {'lab': 'Lab 8'}))
                content = result[0].text if result[0].text else "No data available"
            else:
                content = "I can help with LMS data. Try asking about labs or scores."
            
            response = {
                "id": "chatcmpl-smart",
                "object": "chat.completion",
                "created": 1234567890,
                "model": "coder-model",
                "choices": [{
                    "index": 0,
                    "message": {"role": "assistant", "content": content},
                    "finish_reason": "stop"
                }]
            }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
    
    def do_GET(self):
        if self.path == '/v1/models':
            response = {"object": "list", "data": [{"id": "coder-model", "object": "model"}]}
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 42005), SmartLLMHandler)
    print("Smart LLM server running on port 42005")
    server.serve_forever()
