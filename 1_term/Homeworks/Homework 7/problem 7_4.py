def NSD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    gcd = a + b
    return gcd


def NSK(a, b):
    return a * b // NSD(a, b)


a, b = map(int, input().split())

# version 2 (faster and smarter, but 80% cause time rang out)
"""if b % a != 0 or b <= 0 or a <= 0:
    print(0)
elif a == b:
    print(1)
else:
    ans = 0
    for p in range(a, b + 1, a):
        for q in range(a, p, a):
            if NSD(p, q) == a and NSK(p, q) == b:
                ans += 2
    print(ans)"""

# version 3
if b % a != 0 or b <= 0 or a <= 0:
    print(0)
elif a == b:
    print(1)
else:
    ans = 0
    for p in range(a, b + 1, a):
        if a * b % p != 0:
            continue
        else:
            q = a * b // p
            if NSD(p, q) == a:
                ans += 1
    print(ans)
