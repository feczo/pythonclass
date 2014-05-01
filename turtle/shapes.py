from turtle import *

pendown()


def shape(sides, size, angle):
    for i in range(sides):
        forward(size)
        left(angle)

shape(4, 100, 90)
forward(100)
shape(3, 90, 120)
forward(100)
shape(4, 80, 90)
forward(100)
shape(4, 70, 90)

while True:
    pass
