#!/usr/bin/python3
"""HTTP API server."""

import json
import http.server


class LocalHandler(http.server.BaseHTTPRequestHandler):
    """request handler."""

    def do_GET(self):
        """Handle GET requests"""

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


PORT = 8000

with http.server.HTTPServer(("", PORT), LocalHandler) as httpd:
    print(f"Server running on port {PORT}...")
    httpd.serve_forever()
