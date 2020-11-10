# Виконати наближення функції f(x) на відрізку [a, b] частиною ряду
# Тейлора, що є розкладом f(x) у 0. Взяти перші n доданків для n = 1, 2, …, m,
# де m – задане число. Побудувати графікі функції та її наближення. Зберегти
# відео (виконати анімацію) для різних значень n. Використати масиви numpy.
# Розв’язати задачу для функції f(x) = sqrt(1+x) = 1 + 1/2 x - 1/(2*4)x^2 + 1*3/2*4*6x^3- ...


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

a = -1
b = 1.5
m = 20

x = np.linspace(a, b, int((b - a) * 50))

fig = plt.figure()
ax = plt.axes(xlim=(a, b), ylim=(-1, 3))
line, = ax.plot([], [], lw=3)


def func_m(x, n):
    s = np.ones_like(x) + 0.5 * x.copy()
    t = 0.5 * x.copy()
    for k in range(2, n):
        t *= -x * (2*k - 3) / (2*k)
        s += t
    return s


def init():
    plt.plot(x, np.sqrt(1 + x), "--r")
    line.set_data([], [])
    return line,


def animate(i):
    y = func_m(x, i + 1)
    line.set_data(x, y)
    return line,


anim = FuncAnimation(fig, animate, init_func=init, frames=m, interval=1000, repeat=True)
plt.show()
anim.save("sqrt.gif", writer="pillow")
