n = int(input("n="))
a_0 = int(input("Введіть елемент послідовності "))
a = a_0
b = a_0 ** 2
for i in range(1, n):
    t = int(input("Введіть елемент послідовності "))
    a = min(a, t)
    b = min(b, t ** 2)
c = a ** 2 - b
print(c)