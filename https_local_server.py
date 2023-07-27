import argparse
import ssl
from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        print("HEADERS:", self.headers)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Hi there! Here is a GET response"
        self.wfile.write(bytes(message, "utf8"))
    def do_POST(self):
        self.send_response(200)
        print("HEADERS:", self.headers)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Hello! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))


def main():
    parser = argparse.ArgumentParser(description="HTTPS server in localhost")
    parser.add_argument("-p", "--port", default=8000, help="https assigning port")
    parser.add_argument("-key", "--ca_key_file", required=True, help="CA Key File")
    parser.add_argument("-cert", "--ca_cert_file", required=True, help="CA Cert File")
   
    args = parser.parse_args()
    httpd = HTTPServer(('localhost', args.port), handler)
    httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=args.ca_key_file,certfile=args.ca_cert_file, server_side=True,ssl_version=ssl.PROTOCOL_TLS)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
