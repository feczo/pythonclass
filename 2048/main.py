from numpy import random, array

a = array([[None for i in range(4)] for i in range(4)])

def addblock():
    col = random.randint(4)
    row = random.randint(4)
    if not a[row, col]:
        a[row, col] = 2
    else:
        addblock()


def move(way, collapse=0):
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
    		if not a[curr]:
    		    a[curr] = a[prev]
    	            a[prev] = None
                    change = True
    	        if a[prev] == a[curr]:
    		    a[curr] *= 2
    	            a[prev] = None
		    collapse += 1
		    #if collapse < 2:
		    #    change = True
                    #else:
		    change = False
    if change:
        move(way, collapse)
    else:
        addblock()


addblock()
addblock()

for i in range(4):
	a[0,i] = 2
