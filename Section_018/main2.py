from turtle import Turtle, Screen, colormode
import random

colormode(255)
tim = Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    clr = (r, g, b)
    return clr


colors = ["red", "blue", "brown", "black", "green", "aquamarine", "coral"]
directions = [0, 90, 180, 270]
# Draw a random walk
# With thickness changed as well
tim.pensize(10)
tim.speed("slowest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
