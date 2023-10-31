from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
	<title>SOFTWARE COMPANIES</title>
		<body>
			<table border="3" align="center" cellspacing="4">
			<caption><b>Top Five Revenue Genrating Software Companies</b></caption>
			<tr>
				<th>S.NO</th>
				<th>Company</th>
				<th>Revenue</th>
			</tr>
			<tr>
				<td>1</th>
				<td>Microsoft</td>
				<td>65 Billion</td>
			</tr>
			<tr>
				<td>2</td>
				<td>Oracle</td>
				<td>25 Billion</td>
			</tr>
			<tr>
				<td>3</td>
				<td>IBM</td>
				<td>27.9 Billion</td>
			</tr>
			<tr>
				<td>4</td>
				<td>SAP</td>
				<td>4.9 Billion</td>
			</tr>
			<tr>
				<td>5</td>
				<td>Symantec</td>
				<td>6.5 Billion</td>
			</tr>
			</table>
		</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()