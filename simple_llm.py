from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class LLMHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/v1/chat/completions':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)
            
            messages = data.get('messages', [])
            last_message = messages[-1]['content'] if messages else ""
            
            response = {
                "choices": [{
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": f"Here are the labs from LMS: Lab 8: Software Engineering Toolkit Lab 8"
                    },
                    "finish_reason": "stop"
                }]
            }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
    
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
        elif self.path == '/v1/models':
            response = {"data": [{"id": "coder-model"}]}
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), LLMHandler)
    print("Simple LLM server running on port 8080")
    server.serve_forever()
