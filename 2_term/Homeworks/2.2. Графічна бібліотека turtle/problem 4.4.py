from turtle import *
import time


class TurtleDigit:
    def __init__(self, number):
        self.value = number

    def draw(self, scale=3):
        a = self.value
        s = scale
        if a == 1:
            lt(30), fd(3 * s), rt(120), fd(10 * s), lt(90)
        elif a == 2:
            fd(5 * s), rt(90), fd(5 * s), rt(90), fd(5 * s), lt(90), fd(5 * s), lt(90), fd(5 * s)
        elif a == 3:
            fd(5 * s), rt(90), fd(5 * s), rt(90), fd(5 * s), rt(180), fd(5 * s), rt(90), fd(5 * s), rt(90), fd(
                5 * s), rt(180)
        elif a == 4:
            rt(90), fd(5 * s), lt(90), fd(5 * s), lt(90), fd(5 * s), rt(180), fd(10 * s), lt(90)
        elif a == 5:
            rt(180), fd(5 * s), lt(90), fd(5 * s), lt(90), fd(5 * s), rt(90), fd(5 * s), rt(90), fd(5 * s), rt(180)
        elif a == 6:
            rt(180), fd(5 * s), lt(90), fd(5 * s), lt(90), fd(5 * s), rt(90), fd(5 * s), rt(90), fd(5 * s), rt(90), fd(
                5 * s), rt(90)
        elif a == 7:
            fd(5 * s), rt(90), fd(10 * s), lt(90)
        elif a == 8:
            rt(180), fd(5 * s), lt(90), fd(5 * s), lt(90), fd(5 * s), rt(90), fd(5 * s), rt(90), fd(5 * s), rt(90), fd(
                5 * s), rt(90), fd(5 * s), lt(90), fd(5 * s), rt(90)
        elif a == 9:
            rt(180), fd(5 * s), lt(90), fd(5 * s), lt(90), fd(5 * s), lt(90), fd(5 * s), lt(180), fd(10 * s), rt(90), \
            fd(5 * s), rt(180), fd(5 * s)
        elif a == 10:
            lt(30), fd(3 * s), rt(120), fd(10 * s), lt(90), up(), fd(5 * s), down(), lt(90), fd(10 * s), rt(90), \
            fd(5 * s), rt(90), fd(10 * s), rt(90), fd(5 * s), rt(180), fd(5 * s)
        elif a == 11:
            lt(30), fd(3 * s), rt(120), fd(10 * s), lt(90), up(), fd(7 * s), down(), lt(90), fd(10 * s), lt(120), \
            fd(3 * s), rt(30), rt(180)
        elif a == 12:
            lt(30), fd(3 * s), rt(120), fd(10 * s), lt(90), up(), fd(5 * s), lt(90), fd(10 * s), rt(90), down(), \
            fd(5 * s), rt(90), fd(5 * s), rt(90), fd(5 * s), lt(90), fd(5 * s), lt(90), fd(5 * s)


'''home()
up()
goto(-100, 100)
down()
for i in range(1, 13):
    TurtleDigit(i).draw()
    up()
    fd(25)
    down()
done()'''


home()
speed(50)
up()
rt(90)
fd(200)
lt(90)
down()
circle(200)
up()
goto(0, 0)
lt(90)
angle = 0
for i in range(1, 13):
    angle += 30
    rt(angle)
    up()
    fd(200)
    if i == 12:
        fd(35)
    elif i == 11:
        fd(40)
    elif i == 10:
        fd(50)
    elif i == 1:
        fd(23)
    elif i == 2:
        fd(23)
    else:
        fd(15)
    down()
    lt(angle)
    rt(90)
    if i == 12:
        up(), rt(180), fd(19), rt(180), down()
    elif i == 3 or i == 9:
        lt(90), up(), fd(15), down(), rt(90)
    elif i == 7:
        rt(180), up(), fd(5), down(), rt(180)
    elif i == 5 or i == 6:
        up(), fd(i + 1), down()
    TurtleDigit(i).draw()
    lt(90)
    up()
    goto(0, 0)
    down()
    setheading(90)

shape("turtle")
speed(999999999999999999999999999)
# angel = 0
goto(0, 150)
time.sleep(3)
while True:
    """angel += 6
    angel = angel % 360"""
    time.sleep(1)
    undo()
    rt(6)
    fd(150)
