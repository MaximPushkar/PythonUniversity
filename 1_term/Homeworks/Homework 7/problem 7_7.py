def dif(n):
    q = n % 10
    w = (n // 10) % 10
    e = (n // 100) % 10
    r = (n // 1000) % 10
    if q == w or q == e or q == r or w == e or w == r or e == r:
        return False
    return True


s = list(map(int, input().split()))
a, b = s[0], s[1]

for i in range(a, b + 1):
    if dif(i):
        print(i, end=" ")