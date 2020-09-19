import turtle
import time
import datetime


class Arrow:
    def __init__(self, length, angle, center, value):
        self.length = length
        self.angle = angle
        self.turtle = turtle
        self.center = center
        self.draw(value)

    def draw(self, n):
        turtle.penup()
        turtle.goto(self.center)
        turtle.seth(90 - n * self.angle)
        turtle.pendown()
        turtle.fd(self.length)
        turtle.penup()
        turtle.goto(self.center)

    def erase(self, n):
        turtle.penup()
        turtle.goto(self.center)
        turtle.seth(90 - n * self.angle)
        turtle.pendown()
        turtle.color("white")
        turtle.fd(self.length)
        turtle.color("black")
        turtle.penup()
        turtle.goto(self.center)


turtle.speed(10)
turtle.hideturtle()

turtle.penup()
turtle.goto(0, -120)
turtle.pendown()
turtle.circle(120)
turtle.penup()
turtle.goto(0, 0)

turtle.seth(90)
for i in range(1, 13):
    turtle.goto(-6, -8)
    turtle.right(30)
    turtle.penup()
    turtle.fd(135)
    turtle.pendown()
    turtle.write(i, 8)
    turtle.penup()

now = datetime.datetime.now()

s = now.second
m = now.minute
h = now.hour

second = Arrow(100, 6, (0, 0), s)
minute = Arrow(90, 6, (0, 0), m)
hour = Arrow(50, 30, (0, 0), h)


while True:
    time.sleep(0.7)
    second.erase(s)
    print(s, m, h)
    if (s - m) % 60 == 0:
        minute.draw(m)
    if (s - h) % 60 == 0 or (m - h) % 60 == 0:
        hour.draw(h)
    s += 1
    if s % 60 == 0:
        minute.erase(m)
        m += 1
        minute.draw(m)
        if m % 60 == 0:
            hour.erase(h)
            h += 1
            hour.draw(h)

    second.draw(s)

turtle.done()
