def wcgi_app(env, start_response):
	status = '200 OK'
	html   = "\r\n<h1 style='color:green;'>Hello, World!</h1>\n"
	# html = env['QUERY_STRING'].split('&')
	headers = [
		('Content-type', 'text/html'),
		#('Content-length', str(len(html)))
	]
	start_response(status, headers)
	return [bytes(html, encoding="utf8")]
	#return [bytes("\r\n".join(html), encoding="utf8")]