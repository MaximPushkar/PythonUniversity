def F(n):
    if n == 0:
        return 0
    elif n % 10 > 0:
        return n % 10
    else:
        return F(n//10)


def S(p, q):
    s = 0
    for i in range(p, q + 1):
        s += F(i)
    return s


p, q = int(input()), int(input())
print(S(p, q))