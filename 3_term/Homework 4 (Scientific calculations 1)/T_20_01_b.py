import numpy as np
import matplotlib.pyplot as plt


def func2(n):
    return ((n-1)**4 - (n+2)**4) / ((2*n + 1)**3 - (n - 1)**3)


def gety(f, x):
    n = x.size
    y = np.zeros(n)
    for i in range(n):
        y[i] = f(int(x[i]))
    return y


def vect(f, a, b, step=1):
    n = int(np.ceil((b - a) / step))
    x = np.arange(a, b, step)
    y = np.zeros(n)
    for i in range(n):
        y[i] = f(a + i)
    return x, y


def plot_seq(x, y, b=None, eps=0.01, forall=True):
    if b is None:
        plt.plot(x, y, ".b")
        return y[-1]
    else:
        k = -1
        prev = False
        for i in range(y.size):
            if abs(y[i] - b) < eps:
                if not prev:
                    k = i
                    prev = True
            else:
                prev = False

        if not prev:
            return

        begin = 0 if forall else k

        plt.plot(x[begin:], y[begin:], ".b")
        plt.plot(np.array((x[begin], x[-1])), np.array((b, b)), "-r")
        plt.plot(np.array((x[begin], x[-1])), np.array((b - eps, b - eps)), "--g")
        plt.plot(np.array((x[begin], x[-1])), np.array((b + eps, b + eps)), "--g")

        plt.xlabel("n")
        plt.ylabel("a(n)")
        plt.axis([x[begin], x[-1], b - eps*2, b + eps*2])

        return x[k]


if __name__ == '__main__':
    t = (1, 3000, 1)

    x, y = vect(func2, *t)

    b = -12/7
    eps = 0.001
    print(plot_seq(x, y, b, eps, False))
    plt.show()
