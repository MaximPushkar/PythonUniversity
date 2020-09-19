import turtle


def square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)


def sector(radius, angle):
    turtle.forward(radius)
    turtle.left(90)
    turtle.circle(radius, angle)
    turtle.left(90)
    turtle.forward(radius)
    turtle.left(180 - angle)


def move(x, y):
    turtle.up()
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.right(90)
    turtle.down()


def radioactive(radius1, radius2, side, angle=60, outlinecol="black", fillcol="yellow"):
    turtle.color(outlinecol)
    move(-(side / 2), -(side / 2))

    turtle.begin_fill()
    square(side)
    turtle.color(fillcol)
    turtle.end_fill()
    move((side / 2), (side / 2))
    turtle.color(outlinecol)
    turtle.right(90 + angle / 2)

    for i in range(3):
        turtle.begin_fill()
        sector(radius1, angle)
        turtle.left(120)
        turtle.color(outlinecol)
        turtle.end_fill()

    turtle.up()
    turtle.forward(radius2)
    turtle.left(90)
    turtle.down()

    turtle.color(fillcol)
    turtle.begin_fill()
    turtle.circle(radius2)
    turtle.color(outlinecol)
    turtle.end_fill()

    turtle.up()
    turtle.left(90)
    turtle.forward(radius2)
    turtle.width(1)


turtle.reset()
turtle.width(5)
turtle.speed(100)
radioactive(160, 36, 400)
turtle.mainloop()