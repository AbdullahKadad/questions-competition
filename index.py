from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        msg = "Welcome To Questions Competition"
        self.wfile.write(msg.encode())
        return