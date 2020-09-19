import math
n = int(input("n="))
c = int(math.sqrt(n)) + 2

# вариант 1
p = True
for b in range(c):
    for a in range(b + 1):
        if a ** 2 + b ** 2 == n:
            print(a, b)
            p = False
            break
if p:
    print("таких a, b не існує")


# вариант 2
for b in range(c - 1):
    a = n - b * b
    eps = math.sqrt(a) - int(math.sqrt(a))
    if eps == 0:
        print(int(math.sqrt(a)), b)
        break
else:
    print("таких a, b не існує")