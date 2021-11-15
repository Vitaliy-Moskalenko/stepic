def wcgi_app(env, start_response):
	status = '200 OK'
	# html   = b"Hello, World!\n"
	html = env['QUERY_STRING'].split('&')
	headers = [
		('Content-type', 'text/plain'),
		#('Content-length', str(len(html)))
	]
	start_response(status, headers)
	return [bytes("\r\n".join(html), encoding="utf8")]