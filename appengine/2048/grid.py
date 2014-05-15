import random


class Grid(object):
    def __init__(self):
        self.lol = [[None for i in range(4)] for i in range(4)]
	self.addblock()
	self.addblock()

    def get(self, a, b):
        return self.lol[a][b]

    def content(self):
        return self.lol

    def set(self, cord, value):
        a, b = cord
        self.lol[a][b] = value

    def addblock(self):
        col = random.randint(0, 3)
        row = random.randint(0, 3)
        if not self.get(row, col):
            self.set([row, col], 2)
        else:
            self.addblock()

    def move(self, way):
        change = False
        if way in ['down', 'right']:
            rows = list(reversed(range(1, 4)))
        elif way in ['up', 'left']:
            rows = range(3)

        for col in range(4):
            for row in rows:
                if way == 'down':
                    curr = [row, col]
                    prev = [row-1, col]
                if way == 'up':
                    curr = [row, col]
                    prev = [row+1, col]
                if way == 'left':
                    curr = [col, row]
                    prev = [col, row+1]
                if way == 'right':
                    curr = [col, row]
                    prev = [col, row-1]
                if self.get(*prev):
                    if not self.get(*curr):
                        self.set(curr, self.get(*prev))
                        self.set(prev, None)
                        change = True
                    if self.get(*prev) == self.get(*curr):
                        self.set(curr, self.get(*curr)*2)
                        self.set(prev, None)
                        change = False
        if change:
            self.move(way)
        else:
            self.addblock()


grid = Grid()
