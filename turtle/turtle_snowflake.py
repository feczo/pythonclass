from turtle import *


def koch(depth, size):
    if depth == 0:
        forward(size)
    else:
        recurse = lambda: koch(depth-1, size/3)
        recurse()
        left(60)
        recurse()
        right(120)
        recurse()
        left(60)
        recurse()

koch(3, 3**4)
