from turtle import *


def click(x, y):
    global m
    m = False



def move():
    fd(2)
    if m:
        ontimer(move, 30)


m = True
onscreenclick(click)
move()

done()