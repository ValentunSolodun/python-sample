from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		if self.path=="/":
			self.path="public/home.html"
		if self.path=="/second-page":
			self.path="public/second.html"

		try:
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			f = open(curdir + sep + self.path, 'rb') 
			self.wfile.write(f.read())
			f.close()
		except IOError:
			f = open('public/404.html', 'rb')
			self.wfile.write(f.read())
			self.send_error(404,'File Not Found: %s' % self.path)
			f.close()

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
