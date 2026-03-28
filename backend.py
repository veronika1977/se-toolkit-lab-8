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
                self.end_headers()
                self.wfile.write(b'[{"id":1}]')
            except:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b'{"error":"DB failed"}')
        else:
            self.send_response(404)

HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
