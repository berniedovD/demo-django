from wsgiref.simple_server import make_server

def application(environ, start_response):
    # test
    i = 1;
    print (f"in application {i}")
    for key in environ.keys():
        #print (key)
        pass
    user = environ.get('USER')
    req_method = environ.get("REQUEST_METHOD")
    print (f"{user}  {req_method}") 
    start_response("200 OK", [("Content-type", "text/plain")])
    return ["Hello my friend!".encode("utf-8")]


server = make_server('10.20.4.14', 8080, application)
server.serve_forever()
