n = int(input())
ans = 0
for q in range(n):
    s = list(input())
    p = True
    for i in range(len(s)-1):
        if s[i] == "C" and s[i + 1] == "D":
            p = False
            break
    ans += 1 if p else 0
print(ans)
