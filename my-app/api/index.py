import json
import os
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow CORS
        self.end_headers()

        # Load student data
        with open(os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')) as f:
            students = json.load(f)

        # Parse query parameters
        query = self.path.split('?')[-1]
        names = [pair.split('=')[1] for pair in query.split('&') if 'name=' in pair]

        # Fetch marks
        marks = [students.get(name, 0) for name in names]

        # Send response
        response = json.dumps({"marks": marks})
        self.wfile.write(response.encode('utf-8'))
