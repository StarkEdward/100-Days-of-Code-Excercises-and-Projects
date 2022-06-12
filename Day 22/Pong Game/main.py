from turtle import Screen, Turtle
from paddle import Paddle
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# paddle = Turtle("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(x=350, y=0)

paddle1 = Paddle()
paddle1.create_paddle()


screen.listen()

paddle1.go_up()
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


game_is_on = True
while game_is_on:
    screen.update()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")

screen.exitonclick()