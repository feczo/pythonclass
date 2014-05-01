from turtle import *

pendown()


def angle_calc(sides):
    """Angle Calculator
    
    >>> angle_calc(4)
    90
    """
    return 3600//sides

def shape(sides, size):
    for i in range(sides):
        forward(size)
        left(angle_calc(sides))
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    shape(4, 100)
    while True:
        pass
