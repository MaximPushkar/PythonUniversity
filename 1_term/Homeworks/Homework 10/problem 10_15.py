n = int(input())
s = input()

d = {}
for i in s:
    if i not in d:
        d[i] = s.count(i)

p = True
for i in d.keys():
    if d[i] % 2 != 0:
        t = i
        p = False
        break

if p:
    print("Ok")
else:
    print(t)
