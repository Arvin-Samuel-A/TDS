import json
import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow requests from any origin
        self.end_headers()

        # Load student data from JSON file
        json_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')
        with open(json_path, 'r') as f:
            students = json.load(f)

        # Parse query parameters
        query_params = parse_qs(urlparse(self.path).query)
        names = query_params.get("name", [])  # Get 'name' values from query

        # Extract marks
        marks = []
        for name in names:
            mark = next((s["marks"] for s in students if s["name"] == name), 0)
            marks.append(mark)

        # Response
        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode("utf-8"))
