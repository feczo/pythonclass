import os

import jinja2
import webapp2

from ui import createblock
from grid import *


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


def format(grid):
    blocks = [[None for i in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            blocks[i][j] = createblock(grid.get(i,j))
    return blocks

class MainPage(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('index.html')
        nextmove = None
        try:
            nextmove = self.request.get('move')
            grid.move(nextmove)
        except:
            pass

        blocks = format(grid)
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(blocks=blocks))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
