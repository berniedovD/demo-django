from wsgiref.simple_server import make_server

def application(environ, start_response):
    print ("in application")
    start_response("200 OK", [("Content-type", "text/plain")])
    return ["Hello my friend!".encode("utf-8")]


server = make_server('10.20.4.14', 8080, application)
server.serve_forever()
