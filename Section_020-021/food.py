
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,  stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        threshold = 260
        random_x = random.randint(-threshold, threshold)
        random_y = random.randint(-threshold, threshold)
        self.goto(random_x, random_y)
