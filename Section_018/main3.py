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


# Drawing a Spirograph
tim.speed("fastest")
for _ in range(0, 361, 1):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(_)


# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(20)
#     tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
