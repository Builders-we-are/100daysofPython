
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            # new_turtle.goto(x=(0 - positions * 20), y=0)
            new_turtle.goto(positions)
            self.segments.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
