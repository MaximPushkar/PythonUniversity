from turtle import *

shape('turtle')
speed(0)


def up_press():
    global m
    m += 1


def down_press():
    global m
    m -= 1


def left_press():
    lt(5)


def right_press():
    rt(5)


def move():
    fd(m)
    ontimer(move, 30)


m = 0
listen()
onkey(up_press, "Up")
onkey(down_press, "Down")
onkey(left_press, "Left")
onkey(right_press, "Right")

move()

done()
