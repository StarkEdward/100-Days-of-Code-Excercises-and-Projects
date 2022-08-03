import turtle
import pandas

screen = turtle.Screen()
screen.title("States of India")
image = "Indian_states.gif"
screen.addshape(image)
turtle.shape(image)

ordinate = []

def get_mouse_coordinates(x, y):
    x = ordinate.append(x)
    y = ordinate.append(y)
    # print(x, y)
    print(ordinate)


turtle.onscreenclick(get_mouse_coordinates)
turtle.mainloop()