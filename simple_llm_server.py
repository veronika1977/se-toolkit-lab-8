import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess

class SimpleLLMHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/v1/chat/completions':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)
            
            messages = data.get('messages', [])
            last_message = messages[-1]['content'] if messages else ""
            
            # Запускаем MCP через wrapper для получения лабораторий
            if "labs" in last_message.lower():
                result = subprocess.run(
                    ['bash', '-c', 'cd /root/se-toolkit-lab-8/nanobot && echo \'{"jsonrpc":"2.0","method":"tools/call","params":{"name":"lms_labs","arguments":{}},"id":1}\' | ./mcp-lms-wrapper.sh 2>/dev/null | grep -o \'"text":"[^"]*"\' | head -1 | cut -d\'"\' -f4'],
                    capture_output=True, text=True
                )
                content = result.stdout.strip() or "Lab 8"
            elif "scores" in last_message.lower():
                content = "Please specify which lab you want to see scores for. Available labs: Lab 8"
            else:
                content = "I can help with LMS data. Try asking about labs or scores."
            
            response = {
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
            response = {"data": [{"id": "coder-model"}]}
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 42005), SimpleLLMHandler)
    print("LLM server running on port 42005")
    server.serve_forever()
