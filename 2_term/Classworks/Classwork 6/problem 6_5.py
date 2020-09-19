from turtle import *


def click(x, y):
    global m
    m = not m


def move():
    x = xcor()
    print(x)
    if m:
        fd(2)
    ontimer(move, 30)


m = True
onscreenclick(click)
move()

done()
