import os
from http.server import HTTPServer, BaseHTTPRequestHandler

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>THE DOGMA FX SYSTEM</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body { background: #0f1117; color: #e2e8f0; font-family: Arial; text-align: center; padding: 40px; }
        h1 { font-size: 48px; color: #f1f5f9; }
        .status { color: #22c55e; font-size: 28px; }
        .info { color: #94a3b8; font-size: 16px; }
    </style>
</head>
<body>
    <h1>THE DOGMA FX SYSTEM</h1>
    <div class="status">✅ SYSTEM IS LIVE</div>
    <div class="info">Version 6.0 - Running 24/7 on Render.com</div>
    <div class="info">All 10 layers active</div>
    <div class="info" style="margin-top:20px;font-size:12px;color:#64748b;">"Quality over quantity. Most days = NULL."</div>
</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(HTML.encode())

def run():
    port = int(os.environ.get("PORT", 8080))
    print(f"Starting server on port {port}")
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()

if __name__ == "__main__":
    run()
