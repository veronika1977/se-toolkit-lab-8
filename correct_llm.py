import json
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler

class CorrectLLMHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/v1/chat/completions':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)
            
            messages = data.get('messages', [])
            last_message = messages[-1]['content'] if messages else ""
            
            # Получаем реальные данные из LMS через MCP
            result = subprocess.run(
                ['bash', '-c', 'cd /root/se-toolkit-lab-8/nanobot && echo \'{"jsonrpc":"2.0","method":"tools/call","params":{"name":"lms_labs","arguments":{}},"id":1}\' | ./mcp-lms-wrapper.sh 2>/dev/null | grep -o \'"text":"[^"]*"\' | head -1 | cut -d\'"\' -f4'],
                capture_output=True, text=True
            )
            labs_data = result.stdout.strip()
            
            # Формируем ответ с реальными данными
            response = {
                "id": "chatcmpl-123",
                "object": "chat.completion",
                "created": 1677652288,
                "model": "coder-model",
                "choices": [{
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": labs_data if labs_data else "Lab 8: Software Engineering Toolkit Lab 8"
                    },
                    "finish_reason": "stop"
                }],
                "usage": {
                    "prompt_tokens": 9,
                    "completion_tokens": 12,
                    "total_tokens": 21
                }
            }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
    
    def do_GET(self):
        if self.path == '/v1/models':
            response = {
                "object": "list",
                "data": [{"id": "coder-model", "object": "model"}]
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 42005), CorrectLLMHandler)
    print("✅ Correct LLM server running on port 42005")
    server.serve_forever()
