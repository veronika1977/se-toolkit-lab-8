from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/ws/chat'):
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {"content": "Lab 8: Software Engineering Toolkit Lab 8", "format": "markdown"}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)

    def do_POST(self):
        if self.path == '/ws/chat':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {"content": "Lab 8: Software Engineering Toolkit Lab 8", "format": "markdown"}
            self.wfile.write(json.dumps(response).encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8765), Handler)
    print("✅ Server running on port 8765")
    server.serve_forever()
