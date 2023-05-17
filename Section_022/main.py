from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
# import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()


screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


game_is_on = True
while game_is_on:
    # time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if abs(ball.ycor()) > 280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # needs to bounce
        ball.bounce_x()

    # Detect paddle misses
    if abs(ball.xcor()) > 380:
        ball.reset_position()


screen.exitonclick()
