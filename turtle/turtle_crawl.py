from turtle import *
bgcolor("lightgreen")
shape("turtle")

penup()
size = 20
for i in range(30):
    stamp()             # Leave an impression on the canvas
    size = size + 3     # Increase the size on every iteration
    forward(size)       # Move tess along
    right(24)           # and turn her
    if i % 2 == 0:
        color("red")
    else:
        color("blue")

mainloop()
