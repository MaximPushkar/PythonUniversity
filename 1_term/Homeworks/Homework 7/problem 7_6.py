def to_dec_normal(n, k=2):
    p = 1
    ans = 0
    while n != 0:
        ans = ans + (n % 10) * p
        n = n // 10
        p *= k
    return ans


def to_dec(s, k=2):
    ans = 0
    for i in range(len(s)):
        ans += s[i] * k ** (len(s) - i - 1)
    return ans


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


n = int(input())
s = to_bin(n)
ans = n
for i in range(len(s) - 1):
    l = s[1::] + [s[0]]
    t = to_dec(l)
    ans = t if t > ans else ans
    s = l[::]
print(ans)