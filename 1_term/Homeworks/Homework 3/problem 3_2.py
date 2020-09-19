'''for i in range(1, 10):
    print("5 * ", i, "=", 5 * i)'''

'''import math
i = 0
qwerty = float(input())
while i <= 2 * math.pi:
    print(math.sin(i))
    i += qwerty'''

"""n = int(input("n="))
new = 1
for i in range(1, n+1):
    new *= i
print(new)"""


s = 0
ans = 0
a = float(input("Елемент послідовності = "))
while a != 0:
    s += a
    ans += s
    a = float(input("Елемент послідовності = "))
print(ans)
print(s)