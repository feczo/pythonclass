from wsgiref.simple_server import make_server
from cgi import parse_qs, escape


def application(environ, start_response):

   status = '200 OK'

   # Now content type is text/html
   response_headers = [('Content-Type', 'text/html')]
   start_response(status, response_headers)
   
   out = '''<html>
  <head>
    <title>2048</title>
  </head>

  <body>
    Welcome to 2048

    <table border='1' width='400px'>
      <tr>
        <td width='100px'> </td>
        <td width='100px'>2</td>
        <td width='100px'> </td>
        <td width='100px'> </td>
      </tr>
      <tr>
        <td> </td>
        <td> </td>
        <td>2</td>
        <td> </td>
      </tr>
      <tr>
        <td> </td>
        <td>4</td>
        <td> </td>
        <td> </td>
      </tr>
      <tr>
        <td> </td>
        <td> </td>
        <td> </td>
        <td>2048</td>
      </tr>
    </table>

    <form action='/' method='get'>
      <input type='submit' name='move' value='Up' />
      <input type='submit' name='move' value='Down' />
      <input type='submit' name='move' value='Left' />
      <input type='submit' name='move' value='Right' />
    </form>

  </body>

</html>'''


   get_dict = parse_qs(environ['QUERY_STRING'])

   for key,value in get_dict.items():
       out += "key: %s: value: %s<br>" % (key,value)


   return [out]

httpd = make_server('', 8001, application)
print "Serving on port 8001..."
httpd.serve_forever()
