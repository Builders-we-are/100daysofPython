
from turtle import Turtle, Screen

colors = ["red", "green"]
all_turtles = []

for index, each in enumerate(colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(each)
    new_turtle.goto(x=-230, y=(-120 + index * 50))
    all_turtles.append(new_turtle)


for i in all_turtles:
    print(type(i))
#     print(i.turtle())


# print(Turtle.turtle())
