from turtle import *
import doctest

pendown()


def angle_calc(sides):
    """ Angle calculator
    This will calculate the angles
    >>> angle_calc(4)
    90 
    """
    return 360.0/sides


def shape(sides, size):
    for i in range(sides):
        forward(size)
        left(angle_calc(sides+i))

if __name__ == '__main__':
    doctest.testmod()
    shape(4, 100)
    while True:
        pass
