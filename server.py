from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class Handler(SimpleHTTPRequestHandler):
    """Serves static files for both GET and POST requests."""
    def do_POST(self):
        # Bitrix24 sends POST when opening app in iframe
        # Serve index.html for POST requests too
        self.path = '/index.html'
        return self.do_GET()

port = int(os.environ.get('PORT', 8080))
print(f'Server running on port {port}')
HTTPServer(('0.0.0.0', port), Handler).serve_forever()
