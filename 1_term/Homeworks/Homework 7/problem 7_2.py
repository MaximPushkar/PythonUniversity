l = list(map(int, input().split()))
a, b, c = l[0], l[1], l[2]

x = max(a, b, c)
y = min(a, b, c)

if a != x and a != y:
    print(a)
if b != x and b != y:
    print(b)
if c != x and c != y:
    print(c)
