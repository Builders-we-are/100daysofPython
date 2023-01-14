
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
# user_bet = screen.textinput(
#     title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ").lower()
colors = ["red", "gold", "blue", "green", "purple", "brown"]
all_turtles = []


for index, each in enumerate(colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(each)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=(-120 + index * 50))
    all_turtles.append(new_turtle)
    pass


print(dir(all_turtles))
