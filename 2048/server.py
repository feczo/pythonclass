from static import Cling
from wsgiref.simple_server import make_server
from ui import createblock
from main import *
 
def format(mylist):
  template = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
  <html>
  <head>
  <meta name="author" content="myself">
  <title>My 2048</title>
  <style type="text/css">
  div.myblock {
    color: green;
  }
  span {
    padding-right: 5px;
  }
  </style>
  </head>
  <body>
  <script src="/js/keyboard_input_manager.js"></script>
  <table class="game-container">
  <tr> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> </tr>
  <tr> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> </tr>
  <tr> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> </tr>
  <tr> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> </tr>
  </table>
  </body>
  </html>'''
  content = tuple(map(lambda n: createblock(n), mylist))
  return (template % content)


def simple_app(environ, start_response):
    if environ['PATH_INFO'] == '/js/keyboard_input_manager.js':
        start_response('200 OK', [('content-type','application/javascript')])
        return str(open('js/keyboard_input_manager.js', 'r').read())
    else:
        status = '200 OK'
        headers = [('Content-type', 'text/html')]
        
        start_response(status, headers)
	return format(a.flatten())

httpd = make_server('', 8000, simple_app)
print "Serving on port 8000..."
import threading
threading.Thread(target=httpd.serve_forever).start()

while True:
    nextmove = raw_input('What is your next move? [l,r,u,d] ')
    shorthand = {'l': 'left', 'r': 'right', 'u': 'up', 'd': 'down'}
    move(shorthand[nextmove])
