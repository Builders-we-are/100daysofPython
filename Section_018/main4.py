

from turtle import Turtle, Screen, colormode
import random
import colorgram

colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
# Extracting colorway from Damien Hirst painting
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = r, g, b,
#     rgb_colors.append(new_color)
# print(rgb_colors)


color_list = [
    (149, 75, 51), (223, 201, 137), (55, 93, 123), (165,
                                                    150, 47), (133, 33, 23), (133, 162, 182),
    (50, 118, 87), (197, 92, 75), (72, 44, 37), (17,
                                                 97, 73), (148, 178, 147), (97, 74, 76),
    (161, 144, 157), (232, 176, 164), (55, 47,
                                       49), (38, 62, 72), (182, 205, 173), (153, 18, 22),
    (31, 78, 84), (83, 146, 126), (181, 92, 95), (222,
                                                  178, 180), (35, 67, 95), (15, 70, 63), (106, 126, 154)
]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
