from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/items/':
            # Симулируем проверку PostgreSQL
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            try:
                s.connect(('postgres', 5432))
                s.close()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps([{"id": 1, "title": "Lab 8"}]).encode())
            except:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Database connection failed"}).encode())
        else:
            self.send_response(404)
    
    def do_POST(self):
        self.send_response(500)

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), Handler)
    print("Backend running on port 8000")
    server.serve_forever()
