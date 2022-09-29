
import sys
sys.stdout = sys.stderr
def application(env, start_response):
    print ("in uwsgi applicatiom ------------------------------------------")
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]