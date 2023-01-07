# from turtle import Turtle, Screen

# turtle = Turtle()
# screen = Screen()
# turtle.shape("turtle")

# for _ in range(4):
#     turtle.forward(100)
#     turtle.rt(90)

# # turtle.mainloop()

# screen.exitonclick()


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
