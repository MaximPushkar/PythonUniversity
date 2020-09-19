def tailor_sin(x, eps):
    a = x
    s = a
    count = 1
    while abs(a) >= eps:
        a *= (-1) * (x ** 2) / (2 * count * (2 * count + 1))
        count += 1
        s += a
    return s


