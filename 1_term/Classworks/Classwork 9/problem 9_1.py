import random
import turtle


def draw_a_point(x, y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(1)
    turtle.end_fill()

def midpoint(x1, y1, x2, y2):
    return [(x1+x2)//2, (y1+y2)//2]


N = 10000
x = random.randint(-250, 250)
y = random.randint(-250, 250)

x = 0
y = 0

turtle.home()
turtle.speed(1000000)
draw_a_point(-200, -200)
draw_a_point(200, -200)
draw_a_point(0, 200)
draw_a_point(x, y)


for i in range(N):
    t = random.randint(1, 3)
    if t == 1:
        x, y = midpoint(x, y, -200, -200)[0], midpoint(x, y, -200, -200)[1]
        draw_a_point(x, y)
    elif t == 2:
        x, y = midpoint(x, y, 200, -200)[0], midpoint(x, y, 200, -200)[1]
        draw_a_point(x, y)
    else:
        x, y = midpoint(x, y, 0, 200)[0], midpoint(x, y, 0, 200)[1]
        draw_a_point(x, y)


turtle.done()




