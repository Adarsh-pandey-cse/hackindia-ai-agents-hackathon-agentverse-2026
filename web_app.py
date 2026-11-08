"""
AgentVerse Web Interface Server
Serves the HackIndia UI/UX Design System & Interactive Dashboard.
"""
import http.server
import socketserver
import os
import sys

PORT = int(os.getenv("APP_PORT") or os.getenv("PORT") or 3000)
DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == "/health" or self.path == "/api/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
            return
        super().do_GET()

    def log_message(self, format, *args):
        # Clean logging
        sys.stdout.write(f"[AgentVerse.Web] {self.address_string()} - {format % args}\n")

def run_server():
    print("=" * 72)
    print("  AgentVerse Autonomous AI Agent & ML Pipeline - Web Interface")
    print("  Skill: Design a usable hackathon app (HackIndia 2026)")
    print("=" * 72)
    print(f"[*] Serving interactive UI from: {DIRECTORY}")
    print(f"[+] Access the 3 working screens/flows at: http://localhost:{PORT}")
    print("    - Screen 1: Dashboard & Telemetry (#dashboard)")
    print("    - Screen 2: Task Explorer & Empty State (#tasks)")
    print("    - Screen 3: Diagnostics & Schema Error State (#diagnostics)")
    print("=" * 72)
    print("Press Ctrl+C to stop the server.\n")

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[!] Web server stopped.")

if __name__ == "__main__":
    run_server()
