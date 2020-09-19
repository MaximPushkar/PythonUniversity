n = int(input())
s = 0
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            if a + b + c == n:
                s += 1
print(s)
