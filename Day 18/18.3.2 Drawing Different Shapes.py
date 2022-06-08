import turtle as t
import random
shape = t.Turtle()
colors = ["red", "dark magenta", "hot pink", "gold", "chartreuse", "medium blue", "deep sky blue", "steel blue", "light slate gray", "teal", "medium orchid", "light salmon"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        shape.forward(100)
        shape.right(angle)

for shape_side_n in range(3, 11):
    shape.color(random.choice(colors))
    draw_shape(shape_side_n)
