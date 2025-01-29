import json
import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow requests from any origin
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')  # Allow GET and OPTIONS
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')  # Allow custom headers
        self.end_headers()

        # Load student data from Environment Variable (or file)
        students = json.loads(os.getenv("STUDENTS_JSON", "[]"))

        # Parse query parameters
        query_params = parse_qs(urlparse(self.path).query)
        names = query_params.get("name", []) 

        # Extract marks
        marks = [next((s["marks"] for s in students if s["name"] == name), 0) for name in names]

        # Send response
        self.wfile.write(json.dumps({"marks": marks}).encode("utf-8"))

    def do_OPTIONS(self):
        """Handle preflight requests for CORS"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
