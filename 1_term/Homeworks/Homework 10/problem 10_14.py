def gsd(x, y):
    if x < 0:
        x = - x
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x + y


def result(l):
    l = ' '.join(input().split("/")).split()
    a, b, c, d = int(l[0]), int(l[1]), int(l[3]), int(l[4])

    if l[2] == "+":
        p = a * d + b * c
        q = b * d
        print(p, q)
    else:
        p = a * d - b * c
        q = b * d

    p, q = p // gsd(p, q), q // gsd(p, q)
    return p, q


s = []
while 1:
    l = input()
    try:
        count = int(l[0])
        s.append(result(l))
    except ValueError:
        break

print(s)











"""print(p, end="")
print("/", end="")
print(q, end="")"""