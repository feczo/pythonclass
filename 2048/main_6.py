from numpy import random, array
a = array([[None for i in range(4)] for i in range(4)])

def addblock():
    col = random.randint(4)
    row = random.randint(4)
    if not a[row, col]:
        a[row, col] = 2
    else:
        addblock()

def up_down(way):
    change = False
    if way == 'down':
        rows =  list(reversed(range(1,4)))
    if way == 'up':
        rows =  range(3)

    for col in range(4):
        for row in rows:
	    curr = (row, col)
            if way == 'down':
	         prev = (row-1, col)
            if way == 'up':
	         prev = (row+1, col)
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
        up_down(way)

def up():
    for col in range(4):
        for row in range(2,-1,-1):
	    if a[row+1, col]:
	        if a[row+1, col] == a[row, col]:
		    a[row, col] *= 2
	            a[row+1, col] = None
		if not a[row, col]:
		    a[row, col] = a[row+1, col]
	            a[row+1, col] = None




def left():
    for row in range(4):
        for col in range(2,-1,-1):
	    print a[row, col]
	    if a[row, col+1]:
	        if a[row, col+1] == a[row, col]:
		    a[row, col] *= 2
	            a[row, col+1] = None
		if not a[row, col]:
		    a[row, col] = a[row, col+1]
	            a[row, col+1] = None


addblock()
addblock()

