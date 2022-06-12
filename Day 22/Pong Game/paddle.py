from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.create_paddle()

        self.up = self.go_up()
        self.go_down()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=350, y=0)

    def go_up(self):
       self.ycor() + MOVE_DISTANCE
       self.goto(self.xcor(), )

