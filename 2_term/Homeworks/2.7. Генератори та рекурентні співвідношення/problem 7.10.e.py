import math


eps = 0.0000000001  # точність


def cos(x):
    a = 1
    S = 1
    n = -1
    while abs(a) >= eps:
        n += 2
        a *= - x**2 / (n * (n + 1))
        S += a
    return S


def gen_cos(x):
    a = 1
    S = 1
    n = -1
    yield S, a
    while True:
        n += 2
        a *= - x**2 / (n * (n + 1))
        S += a
        yield S, a


x = float(input("x = "))
print()

print("Recurrently:")
# print("cos(%f) = %f" % (x, cos(x)))
print("cos(" + str(x) + ") = " + str(cos(x)))
print()

print("Generator:")
for s, a in gen_cos(x):
    if abs(a) < eps:
        # print("cos(%f) = %f" % (x, s))
        print("cos(" + str(x) + ") = " + str(s))
        break
print()

print("Library value:")
print("cos(" + str(x) + ") = " + str(math.cos(x)))
