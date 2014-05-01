from numpy import array

a = array([[None for i in range(4)] for i in range(4)])


counter = 0

for i in range(4):
    for j in range(4):
	counter += 1
        a[i,j] = counter

print a
