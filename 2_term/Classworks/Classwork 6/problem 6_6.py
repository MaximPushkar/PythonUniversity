from turtle import *


def click(x, y):
    seth(towards(x, y))  # повернуться в сторону точки с координатами (x,y)


def move():
    fd(2)
    ontimer(move, 30)


onscreenclick(click)
move()

done()
