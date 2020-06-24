#DRAWING A SQUARE IN TURTLE BY USING FOR LOOP

import turtle
wn=turtle.Screen()
wn.bgcolor("hotpink")
t=turtle.Turtle()
t.shape("turtle")
t.pensize(5)
t.color("blue")

for i in [1,2,3,4]:
    t.stamp()
    t.forward(100)
    t.right(90)

wn.exitonclick()
