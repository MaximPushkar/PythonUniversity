from turtle import *


class Figure:
    def __init__(self, x, y, color):
        """:param x: координата x положення фігури
        :param y: координата y положення фігури
        :param color: колір фігури
        """
        self._x = x  # _x - координата x
        self._y = y  # _y - координата y
        self._visible = False  # _visible - чи є фіруга видимою на екрані
        self._color = color  # _color - колір фігури

    def draw(self, color):
        """
        :param color: колір
        """
        pass

    def show(self):
        """ Зображує фігуру на екрані """
        if not self._visible:
            self._visible = True
            self.draw(self._color)

    def hide(self):
        """ Ховає фігуру (робить її невидимою на екрані) """
        if self._visible:
            self._visible = False
            # щоб сховати фігуру, потрібно
            # зобразити її кольором фону.
            self.draw(bgcolor())


class Cross(Figure):
    def __init__(self, x, y, color, a):
        super().__init__(x, y, color)
        self.a = a

    def draw(self, color):
        pencolor(color)
        width(15)
        up()
        setpos(self._x, self._y)
        down()
        goto(self._x + self.a / 2.1, self._y + self.a / 2.1)
        goto(self._x - self.a / 2.1, self._y - self.a / 2.1)
        up()
        goto(self._x - self.a / 2.1, self._y + self.a / 2.1)
        down()
        goto(self._x + self.a / 2.1, self._y - self.a / 2.1)
        up()


class Circle(Figure):
    def __init__(self, x, y, r, color):
        super().__init__(x, y, color)
        self._r = r

    def draw(self, color):
        pencolor(color)
        width(15)
        up()
        setpos(self._x, self._y - self._r / 2)
        down()
        circle(self._r / 2)
        up()


class Board3(Figure):
    def __init__(self, x, y, color, size):
        super().__init__(x, y, color)
        self.size = size

    def draw(self, color):
        pencolor(color)
        up()
        setpos(self._x - self.size / 2, self._y - self.size / 2)
        down()
        fillcolor('#{:0>2x}{:0>2x}{:0>2x}'.format(100, 150, 80))
        begin_fill()
        fd(self.size), lt(90), fd(self.size), lt(90), fd(self.size), lt(90), fd(self.size), lt(90)
        end_fill()
        up(), lt(180), fd(self.size / 3), lt(180)
        for i in range(4):
            pencolor("black")
            width(5)
            fd(self.size / 3), lt(90), down(), fd(self.size), lt(180), fd(self.size), lt(90), up()
        setpos(self._x - self.size / 2, self._y - self.size / 2)
        rt(90), fd(self.size / 3), lt(180)
        for i in range(4):
            pencolor("black")
            width(5)
            fd(self.size / 3), rt(90), down(), fd(self.size), rt(180), fd(self.size), rt(90), up()
        rt(90)


"""def simple_put_something(x, y):
    global m
    if m % 2 == 0:
        Cross(x, y, "red", 95).draw("red")
    else:
        Circle(x, y, 95, "blue").draw("blue")
    m += 1"""


def player_wins(person):
    color("black")
    up(), goto(0, 200), down()
    width(5)
    style = ('Courier', 30, 'italic')
    write("Player " + person + " wins!", font=style, align='center')


def it_is_a_draw():
    color("black")
    up(), goto(0, 200), down()
    width(5)
    style = ('Courier', 30, 'italic')
    write("It\'s a draw!", font=style, align='center')
