n = int(input())

l = []
while n != 0:
    i = n % 10
    n = n // 10
    l.append(i)
l = l[::-1]

ans = 0
if len(l) % 2 == 0:
    for i in range(0, len(l) // 2):
        if l[i] == l[len(l) - i - 1]:
            ans += 1
else:
    for i in range(0, (len(l) - 1) // 2):
        if l[i] == l[len(l) - i - 1]:
            ans += 1
    ans += 1
print(ans)