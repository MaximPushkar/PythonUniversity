import random
import turtle


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def colour_triangle(self, colour):
        turtle.up()
        turtle.goto(self.x1, self.y1)
        turtle.color(colour)
        turtle.begin_fill()
        turtle.down()
        turtle.goto(self.x2, self.y2)
        turtle.goto(self.x3, self.y3)
        turtle.goto(self.x1, self.y1)
        turtle.end_fill()


turtle.home()
turtle.speed(10000000000000)
list_colour = ["red", "grey", "black", "purple", "green", "orange", "brown", "blue", "violet", "pink", "yellow"]
while True:
    x1, y1, x2, y2, x3, y3 = random.randint(-250, 250), random.randint(-250, 250), random.randint(-250, 250), random.randint(-250, 250), random.randint(-250, 250), random.randint(-250, 250)
    trian = Triangle(x1, y1, x2, y2, x3, y3)
    colour = random.choice(list_colour)
    trian.colour_triangle(colour)