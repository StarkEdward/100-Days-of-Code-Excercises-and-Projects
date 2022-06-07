from turtle import Turtle, Screen

square = Turtle()
square.shape("turtle")
square.color("orange red")

# square.forward(100)
# square.left(90)
# square.forward(100)
# square.left(90)
# square.forward(100)
# square.left(90)
# square.forward(100)

for turn in range(4):
    square.forward(100)
    square.left(90)



screen = Screen()
screen.exitonclick()