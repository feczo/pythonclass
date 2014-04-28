from wsgiref.simple_server import make_server

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def format(mylist):
  template = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
  <html>
  <head>
  <meta name="author" content="myself">
  <title>Sample page</title>
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
  <div class="myblock">%s</div>
  </body>
  </html>'''
  content = ''.join(map(lambda n: ('<span>%s,</span>' % n), mylist))
  return (template % content)

# A relatively simple WSGI application. It's going to print out the
# first 10 Fibonacci numbers
def simple_app(environ, start_response):

    status = '200 OK'
    headers = [('Content-type', 'text/html')]

    start_response(status, headers)
    out = []
    for i in range(1,10):
        out.append(fib(i))

    return format(out)

httpd = make_server('', 8000, simple_app)
print "Serving on port 8000..."
httpd.serve_forever()


