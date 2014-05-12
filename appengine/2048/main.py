import os

import jinja2
import webapp2

from ui import createblock
from grid import *


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def format(grid):
    content = tuple(map(lambda cell: createblock(cell), grid))
    return content


class MainPage(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('index.html')
        nextmove = None
        try:
            nextmove = self.request.get('move')
        except:
            pass
        if nextmove:
            move(get_dict['move'][0])

        blocks = format(grid.flatten())
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(blocks=blocks))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
