from turtle import *
import random


class Figure:
    """ Клас Фігура """

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
        """ Допоміжний віртуальний метод, що зображує фігуру заданим кольором
        Тут здійснюється лише декларація методу, а конкретна
        реалізація буде здійснюватися у конкретних нащадках
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

    def move(self, dx, dy):
        """ Переміщує об'єкт
        :param dx: зміщення у пікселях по осі X
        :param dy: зміщення у пікселях по осі Y
        """
        isVisible = self._visible
        if isVisible:
            self.hide()
        self._x += dx
        self._y += dy
        if isVisible:
            self.show()


######################  клас Circle  ###########################
################################################################
class Circle(Figure):
    """ Клас Коло """

    def __init__(self, x, y, r, color):
        """ Конструктор
        Ініціалізує положення кола, його радіус і колір
        :param x: координата x центру кола
        :param y: координата y центру кола
        :param r: радіус кола
        :param color: колір кола
        """
        super().__init__(x, y, color)  # Обов’язковий виклик конструктора базового класу
        self._r = r  # r - радіус кола

    def draw(self, color):
        """ Допоміжний метод, що зображує коло заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        # малює починаючи знизу кола
        setpos(self._x, self._y - self._r)
        down()
        circle(self._r)
        up()


#################### клас Quadrate  ############################
################################################################

class Square(Figure):
    """ Клас Квадрат """

    def __init__(self, x, y, a, color):
        """ Конструктор
        Ініціалізує положення лівого нижнього кута квадрата,
        довжину його сторони і колір.
        :param x: координата x лівого нижнього кута квадрата
        :param y: координата y лівого нижнього кута квадрата
        :param a: довжина сторони квадрата
        :param color: колір квадрата
        """
        super().__init__(x, y, color)  # виклик конструктора базового класу
        self.a = a

    def draw(self, color):
        """ Допоміжний метод, що зображує квадрат заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        # малює починаючи знизу кола
        setpos(self._x, self._y)
        down()
        fd(self.a), lt(90), fd(self.a), lt(90), fd(self.a), lt(90), fd(self.a), lt(90)
        up()


#################### клас Triangle  ############################
################################################################

class Triangle(Figure):
    """ Клас Трикутник
    Використовується для зображення правильного трикутника на екрані
    """

    def __init__(self, x, y, a, color):
        """ Конструктор
        Ініціалізує положення лівого нижньої вершини трикутника,
        довжину його сторони і колір.
        :param x: координата x лівої нижньої вершини трикутника
        :param y: координата y лівої нижньої вершини трикутника
        :param a: довжина сторони трикутника
        :param color: колір квадрата
        """

        super().__init__(x, y, color)  # виклик конструктора базового класу
        self.a = a

    def draw(self, color):
        """ Допоміжний віртуальний метод, що зображує трикутник заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        # малює починаючи знизу кола
        setpos(self._x, self._y)
        down()
        fd(self.a), lt(120), fd(self.a), lt(120), fd(self.a), lt(120)
        up()


#################### клас Triangle  ############################
################################################################

class Trapezoid(Figure):
    """ Клас Трапеція
    Використовується для зображення рівнобічної трапеції на екрані
    """

    def __init__(self, x, y, a, b, color):
        """ Конструктор
        Ініціалізує положення лівої нижньої вершини,
        довжини його основ і колір.
        :param x: координата x лівої нижньої вершини
        :param y: координата y лівої нижньої вершини
        :param a: довжина більшох основий трапеції
        :param b: довжина меншої основий трапеції
        :param color: колір квадрата
        """

        super().__init__(x, y, color)  # виклик конструктора базового класу
        self.a = a
        self.b = b

    def draw(self, color):
        """ Віртуальний метод, що зображує трапецію на екрані заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        # малює починаючи знизу кола
        setpos(self._x, self._y)
        down()
        fd(self.a), lt(120), fd((self.a + self.b) / 2), lt(60), fd(self.b)
        goto(self._x, self._y)
        up()



################################################################
################################################################
# Перевірка роботи описаних класів.
speed(100)
"""if __name__ == '__main__':
    # Ініціалізація turtle
    home()
    delay(30)

    ###### Перевірка кола ############
    c = Circle(120, 120, 50, "blue")
    c.show()
    c.move(-30, -140)
    c.hide()

    ###### Перевірка квадрата ############
    q = Quadrate(0, 0, 150, "red")
    q.show()
    q.move(0, 140)
    q.hide()

    ###### Перевірка трикутника ############
    t = Triangle(120, 120, 50, "blue")
    t.show()
    t.move(-30, -140)
    t.hide()

    ###### Перевірка трапеції ############
    t = Trapezoid(120, 120, 50, 30, "blue")
    t.show()
    t.move(-30, -140)
    t.hide()

    mainloop()"""

home()
for i in range(100):
    q = random.randint(1, 4)
    colour = '#{:0>2x}{:0>2x}{:0>2x}'.format(random.randint(0, 254), random.randint(0, 254), random.randint(0, 254))
    if q == 1:
        r = random.randint(20, 80)
        x = random.randint(-150, 150)
        y = random.randint(-150, 150)
        t = Circle(x, y, r, colour)
        t.draw(colour)
    elif q == 2:
        r = random.randint(20, 80)
        x = random.randint(-150, 150)
        y = random.randint(-150, 150)
        t = Square(x, y, r, colour)
        t.draw(colour)
    elif q == 3:
        r = random.randint(20, 80)
        x = random.randint(-150, 150)
        y = random.randint(-150, 150)
        t = Triangle(x, y, r, colour)
        t.draw(colour)
    else:
        r = random.randint(20, 80)
        w = random.randint(20, 80)
        x = random.randint(-150, 150)
        y = random.randint(-150, 150)
        t = Trapezoid(x, y, r, w, colour)
        t.draw(colour)
done()
