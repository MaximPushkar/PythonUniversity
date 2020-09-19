import math


def f(x):
    return math.cos(x)


a = 0
b = f(a)
eps = float(input())
while abs(a - b) >= eps:
    a = b
    b = f(b)
print(a)
print(f(a))

