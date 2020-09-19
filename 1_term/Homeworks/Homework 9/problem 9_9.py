def f(n):
    if n % 2 == 0:
        return f(n // 2)
    else:
        return n


l = [input()]
for i in range(100500):
    a = input()
    if a == "":
        break
    else:
        l.append(a)

s = [int(i) for i in l]
m = max(s)

res = [0 for i in range(len(s))]
ans = 0
for i in range(1, m + 1):
    ans += f(i)
    for j in range(len(res)):
        if s[j] == i:
            res[j] = ans

for i in res:
    print(i)
