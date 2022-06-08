import turtle as t
import random

walk = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color



direction = [0, 90, 180, 270]
walk.pensize(12)
walk.speed("fastest")
for _ in range(200):
    walk.color(random_color())
    walk.forward(30)
    walk.setheading(random.choice(direction))

screen = t.Screen()
screen.exitonclick()