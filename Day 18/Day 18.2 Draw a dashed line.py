# line 10 spaces
# black 10
# total 50 times

from turtle import Turtle, Screen

line = Turtle()
for _ in range(50):
    line.forward(10)
    line.penup()
    line.forward(10)
    line.pendown()



screen = Screen()
screen.exitonclick()