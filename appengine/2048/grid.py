#from numpy import random, array

grid = array([[None for i in range(4)] for i in range(4)])

def grid(a,b):
    return lol[a][b]

def addblock():
    col = random.randint(4)
    row = random.randint(4)
    if not grid[row, col]:
        grid[row, col] = 2
    else:
        addblock()


def move(way, collapse=0):
    print way
    change = False
    if way in ['down', 'right']:
        rows =  list(reversed(range(1,4)))
    elif way in ['up', 'left']:
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
    	    if grid[prev]:
    		if not grid[curr]:
    		    grid[curr] = grid[prev]
    	            grid[prev] = None
                    change = True
    	        if grid[prev] == grid[curr]:
    		    grid[curr] *= 2
    	            grid[prev] = None
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
