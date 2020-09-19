ans = 0
for i in range(10, 100):
    a = i % 10
    b = i // 10
    ans = a ** 2 + b ** 2
    if ans == i:
        print(i)

print("------------")

ans = 0
a = 0
for i in range(100, 1000):
    p = i
    for j in range(1, 4):
        a = i % 10
        i = ((i - a) // 10)
        ans += a ** 3
    if ans == p:
        print(p)
    ans = 0

print("------------")

ans = 0
a = 0
for i in range(1000, 10000):
    p = i
    for j in range(1, 5):
        a = i % 10
        i = ((i - a) // 10)
        ans += a ** 4
    if ans == p:
        print(p)
    ans = 0

print("------------")