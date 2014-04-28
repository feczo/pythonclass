import pdb


def add(a, b):
    if (__debug__ and b != 1):
        print 'B is not one! b = %d' % b
        pdb.set_trace()
    return a+b

print add(1, 2)
