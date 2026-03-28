from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import socket

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/items/':
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect(('postgres', 5432))
                s.close()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps([{"id": 1, "title": "Lab 8"}]).encode())
            except Exception as e:
                print(f"DB error: {e}")
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Database connection failed"}).encode())
        else:
            self.send_response(404)

print("Backend starting...")
HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
