s = input("string=")

t = s.split("+")
p = []
for i in t:
    p.extend(i.split("-"))
print(p)

ans = 0
for i in p:
    ans += int(i)
print(ans)
