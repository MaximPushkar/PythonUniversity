a = float(input())
s = 0
i = 1
while s < a:
    s += 1 / i
    i += 1
print(i - 1)
print(s)