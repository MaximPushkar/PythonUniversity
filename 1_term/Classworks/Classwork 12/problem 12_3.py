def square_root_1(x, eps):
    x0 = x / 2
    x1 = (1 / 2) * (x0 + x / x0)
    while abs(x0 - x1) >= eps:
        x0, x1 = x1, (1 / 2) * (x1 + x / x1)
    return x1


def square_root_2(x, eps):
    x0 = x / 2
    while abs(x0 ** 2 - x) >= eps:
        x0 = (1 / 2) * (x0 + x / x0)
    return x0


print(square_root_1(9, 0.00001))
print(square_root_2(9, 0.00001))


