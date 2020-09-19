import math

n = int(input())
f = 1
for i in range(2, n + 1):
    f *= i

p = True

for i in range(1, int(f ** (1 / 3)) + 1):
    if i * (i + 1) * (i + 2) == f:
        print("yes")
        print(i, " * ", i + 1, " * ", i + 2, " = ", f)
        p = False
        break
if p:
    print("no")