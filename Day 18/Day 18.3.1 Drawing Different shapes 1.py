from turtle import Turtle, Screen
import random
shapes = Turtle()


def triangle():
    shapes.color("blue")
    for _ in range(3):
        shapes.forward(100)
        shapes.right(120)


def square():
    shapes.color("orange")
    for _ in range(4):
        shapes.forward(100)
        shapes.right(90)


def pentagon():
    shapes.color("lime green")
    for _ in range(5):
        shapes.forward(100)
        shapes.right(72)


def hexagon():
    shapes.color("gold")
    for _ in range(6):
        shapes.forward(100)
        shapes.right(60)


def septagon():
    shapes.color("deep sky blue")
    for _ in range(7):
        shapes.forward(100)
        shapes.right(51.43)


def octogon():
    shapes.color("light coral")
    for _ in range(8):
        shapes.forward(100)
        shapes.right(45)


def nonagon():
    shapes.color("orange")
    for _ in range(9):
        shapes.forward(100)
        shapes.right(40)


def decagon():
    shapes.color("blue violet")
    for _ in range(10):
        shapes.forward(100)
        shapes.right(36)


triangle()
square()
pentagon()
hexagon()
septagon()
octogon()
nonagon()
decagon()
screen = Screen()
screen.exitonclick()

