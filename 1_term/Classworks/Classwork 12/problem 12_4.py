def func(n):
    a = 1
    b = 2
    c = 0
    s = a + b + c
    for i in range(n - 3):
        a, b, c = b, c, 2 * c + b - a
        s += c
    return s


s = func(41)
print(s)
