# rule of fast calculate of x to the power of n. Here "S" means square and "X" means multiply by x


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
ans = []
for i in range(1, len(to_bin(n))):
    if to_bin(n)[i] == 1:
        ans.append("SX")
    else:
        ans.append("S")

for i in ans:
    print(i, end="")