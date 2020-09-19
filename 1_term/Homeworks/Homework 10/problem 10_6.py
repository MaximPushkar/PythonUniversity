l = input()
l = " ".join(l.split("/")).split()
a, b, p, q = int(l[0]), int(l[1]), int(l[2]), int(l[3])

x = a / b
y = p / q

if x > y:
    print(p, end="")
    print("/", end="")
    print(q, end=" ")
    print(a, end="")
    print("/", end="")
    print(b, end="")
else:
    print(a, end="")
    print("/", end="")
    print(b, end=" ")
    print(p, end="")
    print("/", end="")
    print(q, end="")