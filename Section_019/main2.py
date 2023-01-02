from turtle import Turtle, Screen
import random
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ").lower()
colors = ["red", "gold", "blue", "green", "purple", "brown"]
all_turtles = []


for index, each in enumerate(colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(each)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=(-120 + index * 50))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        turtle.speed("fastest")

        if turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            print(winning_color)
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(
                    f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# print(list(all_turtles))
# new_turtle.penup()
# new_turtle.goto(x=0, y=0)
# print(user_bet)
screen.exitonclick()
