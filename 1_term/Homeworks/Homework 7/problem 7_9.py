def to_bin(n):
    t = 0
    while 2 ** t <= n:
        t += 1
    s = [0 for i in range(t)]
    s[0] = 1
    n -= 2 ** (t - 1)
    for i in range(1, t):
        if 2 ** (t - i - 1) <= n:
            s[i] = 1
            n -= 2 ** (t - i - 1)
    return s


def answer(n):
    t = to_bin(n)
    ans = 0
    counter = 0
    for i in range(len(t)):
        if t[i] != 0:
            r = len(t) - i - 1
            ans += int(r * 2 ** (r - 1) + 1) + int(counter * 2 ** r)
            counter += 1
    return int(ans)


def count(l):
    ans = 0
    for i in l:
        if i == 1:
            ans += 1
    return ans


a, b = map(int, input().split())
print(answer(b) - answer(a) + count(to_bin(a)))
