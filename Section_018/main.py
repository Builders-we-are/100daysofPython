import heroes
from turtle import Turtle, Screen
import random

tim = Turtle()
# tim.shape("turtle")
# tim.color("red")

# Drawing a Square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Drawing a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# screen = Screen()
# screen.exitonclick()
colors = ["red", "blue", "brown", "black", "green", "aquamarine", "coral"]


def draw_shape(i):
    for _ in range(i):
        tim.forward(100)
        tim.right(360/i)


for _ in range(4, 10):
    tim.color(random.choice(colors))
    draw_shape(_)

# print(Screen.canvheight)
# my_screen.exitonclick()

# for i in range(0, 50):
#     print(heroes.gen())
