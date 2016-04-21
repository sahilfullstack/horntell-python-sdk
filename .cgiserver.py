#!/usr/bin/env python3
import http
from http.server import CGIHTTPRequestHandler, HTTPServer

handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin', '/htbin']  # this is the default
server = HTTPServer(('localhost', 8081), handler)
server.serve_forever()