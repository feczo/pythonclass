def add(a,b=0):
    try:
        return a+b
    except TypeError:
        print 'Do not know how to add different types'

add(3,'b')
