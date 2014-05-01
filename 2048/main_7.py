from numpy import random, array

a = array([[None for i in range(4)] for i in range(4)])

def addblock():
    col = random.randint(4)
    row = random.randint(4)
    if not a[row, col]:
        a[row, col] = 2
    else:
        addblock()


def move(way):
    change = False
    if way in ['down', 'right']:
	rows =  list(reversed(range(1,4)))
    if way in ['up', 'left']:
        rows =  range(3)

    for col in range(4):
        for row in rows:
            if way == 'down':
	         curr = (row, col)
	         prev = (row-1, col)
            if way == 'up':
	         curr = (row, col)
	         prev = (row+1, col)
            if way == 'left':
	         curr = (col, row)
	         prev = (col, row+1)
            if way == 'right':
	         curr = (col, row)
	         prev = (col, row-1)
    	    if a[prev]:
    	        if a[prev] == a[curr]:
    		    a[curr] *= 2
    	            a[prev] = None
                    change = True
    		if not a[curr]:
    		    a[curr] = a[prev]
    	            a[prev] = None
                    change = True
    if change:
        move(way)
    else:
        addblock()


addblock()
addblock()
