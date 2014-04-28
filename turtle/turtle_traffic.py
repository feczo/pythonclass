from turtle import *

setup(400, 500)
title("Tess becomes a traffic light!")
bgcolor("lightgreen")


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    pensize(3)
    color("black", "darkgrey")
    begin_fill()
    forward(80)
    left(90)
    forward(200)
    circle(40, 180)
    forward(200)
    left(90)
    end_fill()


draw_housing()

penup()
# Position onto the place where the green light should be
forward(40)
left(90)
forward(50)
# Turn into a big green circle
shape("circle")
shapesize(3)
fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change  position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        forward(70)
        fillcolor("orange")
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        forward(70)
        fillcolor("red")
        state_num = 2
    else:                    # Transition from state 2 to state 0
        back(140)
        fillcolor("green")
        state_num = 0

# Bind the event handler to the space key.
onkey(advance_state_machine, "space")

listen()                      # Listen for events
mainloop()
