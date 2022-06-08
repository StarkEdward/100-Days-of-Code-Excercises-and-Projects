import turtle as t
import random

walk = t.Turtle()
colors = ["red", "dark magenta", "hot pink", "gold", "chartreuse", "medium blue", "deep sky blue","IndianRed", "steel blue", "light slate gray", "teal", "medium orchid", "light salmon"]

direction = [0, 90, 180, 270]
walk.pensize(15)
walk.speed("fastest")
for _ in range(200):
    walk.color(random.choice(colors))
    walk.forward(30)
    walk.setheading(random.choice(direction))

screen = t.Screen()
screen.exitonclick()