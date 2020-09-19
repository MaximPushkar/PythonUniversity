"""name = input("Введите что-нибудь:  ")
try:
    name = int(name)
    print("Вы ввели целое число")
except ValueError:
    try:
        name = float(name)
        print("Вы ввели дробное число")
    except ValueError:
        print("Вы ввели не число")

while True:
    count = input()
    try:
        count = int(count)
        break
    except ValueError:
        print('Вводите число')"""

import math


n = 100000000  # is working about 7 minutes
p = [True] * (n + 1)
p[0] = False
p[1] = False

for i in range(2, int(n ** (1 / 2)) + 1):
    if p[i]:
        j = 0
        while i ** 2 + j * i <= n:
            p[i ** 2 + j * i] = False
            j += 1


'''for i in range(len(p)):
    if p[i]:
        print(i, end=" ")'''


print(p.count(True) / (n / math.log(n)))

