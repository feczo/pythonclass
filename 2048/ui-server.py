from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
from ui import createblock
from main import *
 
def format(grid):
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

  <form action='/' method='get'>
    <input type='submit' name='move' value='up' />
    <input type='submit' name='move' value='down' />
    <input type='submit' name='move' value='left' />
    <input type='submit' name='move' value='right' />
  </form>
  
  </body>
  </html>'''
  #content = tuple(map(lambda cell: createblock(cell), grid))
  content = tuple(map(lambda cell: cell, grid))
  return (template % content)


def simple_app(environ, start_response):
    if environ['PATH_INFO'] == '/js/keyboard_input_manager.js':
        start_response('200 OK', [('content-type','application/javascript')])
        return str(open('js/keyboard_input_manager.js', 'r').read())
    else:
        status = '200 OK'
        headers = [('Content-type', 'text/html')]

        get_dict = parse_qs(environ['QUERY_STRING'])

	if 'move' in get_dict.keys():
           move(get_dict['move'][0])
        
        start_response(status, headers)
	return format(grid.flatten())

httpd = make_server('', 8004, simple_app)
print "Serving on port 8004..."
import threading
threading.Thread(target=httpd.serve_forever).start()

