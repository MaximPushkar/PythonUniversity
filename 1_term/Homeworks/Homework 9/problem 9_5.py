def p(x):
    return a*x*x*x+b*x*x+c*x+d


a, b, c, d = map(int, input().split())
left = -2.5
right = 2.5
eps = 10 ** (-12)
if (a > 0) or (a == 0 and b > 0) or (a == 0 and b == 0 and c > 0):
    while p(right) < 0:
        right += 1
    while p(left) > 0:
        left -= 1
    q, r = left, right
    while r - q > eps:
        if p((r + q) / 2) >= 0:
            r = (r + q) / 2
        else:
            q = (r + q) / 2
else:
    while p(right) > 0:
        right += 1
    while p(left) < 0:
        left -= 1
    q, r = left, right
    while r - q > eps:
        if p((r + q) / 2) >= 0:
            q = (r + q) / 2
        else:
            r = (r + q) / 2
print(q)

