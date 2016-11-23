def app(environ, start_response):
    """Simplest possible application object"""
    data = environ['QUERY_STRING'].split('&')
    data = [item.encode() for item in data]
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
    ]
    start_response(status, response_headers)
    return iter(data)
