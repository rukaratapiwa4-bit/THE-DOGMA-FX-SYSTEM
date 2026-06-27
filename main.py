import os
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello World - THE DOGMA FX SYSTEM")

server = HTTPServer(("0.0.0.0", int(os.environ.get("PORT", 8080))), Handler)
print("Server running on port", int(os.environ.get("PORT", 8080)))
server.serve_forever()
