def turn_right():
    for n in range (0,3):
        turn_left()
while bool(at_goal()) != True:
    if wall_on_right()==True and wall_in_front()==True:
        turn_left()
    elif wall_on_right() == True:
        move()
    elif wall_on_right() == False:
        turn_right()
        move()
       


 