from turtle import *


def draw_multicolor_square(sz):
    """Make turtle t draw a multi-color square of sz."""
    for i in ["red", "purple", "hotpink", "blue"]:
        color(i)
        forward(sz)
        left(90)

bgcolor("lightgreen")

pensize(3)

size = 20                   # Size of the smallest square
for i in range(15):
    draw_multicolor_square(size)
    size = size + 10        # Increase the size for next time
    forward(10)        # Move along a little
    right(18)          # and give her some turn

mainloop()
