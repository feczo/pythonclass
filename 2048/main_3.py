from numpy import random
a = [[None for i in range(4)] for i in range(4)]


def addblock():
    col = random.randint(4)
    row = random.randint(4)
    if not a[row][col]:
        a[row][col] = 2
    else:
        addblock()

def down():
    for col in range(4):
        for row in reversed(range(1,4)):
	    if a[row-1][col]:
	        if a[row-1][col] == a[row][col]:
		    a[row][col] *= 2
	            a[row-1][col] = None
		if not a[row][col]:
		    a[row][col] = a[row-1][col]
	            a[row-1][col] = None

def up():
    for col in range(4):
        for row in range(3):
	    if a[row+1][col]:
	        if a[row+1][col] == a[row][col]:
		    a[row][col] *= 2
	            a[row+1][col] = None
		if not a[row][col]:
		    a[row][col] = a[row+1][col]
	            a[row+1][col] = None


def left():
    for row in range(4):
        for col in range(3):
	    if a[row][col+1]:
	        if a[row][col+1] == a[row][col]:
		    a[row][col] *= 2
	            a[row][col+1] = None
		if not a[row][col]:
		    a[row][col] = a[row][col+1]
	            a[row][col+1] = None


addblock()
addblock()

a = [[2, 2, None, None],
[None, None, None, None],
[2, None, None, None],
[2, 2, None, None]]

