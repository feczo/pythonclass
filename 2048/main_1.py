from numpy import random
a = [[None for i in range(4)] for i in range(4)]


def addblock():
    col = random.randint(4)
    row = random.randint(4)
    if not a[row][col]:
        a[row][col] = 2
    else:
        addblock()

addblock()
addblock()

