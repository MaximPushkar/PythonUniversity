def gsd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


l = input()
l = " ".join(l.split("/")).split()
a, b, p, q, n = int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4])

x = a * q + p * (n - 1) * b
y = b * q
d = gsd(x, y)
x = x // d
y = y // d

print(x, end="")
print("/", end="")
print(y, end="")
