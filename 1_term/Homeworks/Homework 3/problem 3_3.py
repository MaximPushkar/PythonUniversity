'''n = int(input("n="))
m = int(input("m="))
d = 1
i = 1
t = min(n // 2 + 1, m // 2 + 1)
for i in range(1, t + 1, 1):
    if n % i == 0 and m % i == 0:
        d = i
if m % n == 0:
    d = n
elif n % m == 0:
    d = m
print(d)'''



a = float(input("Елемент послідовності = "))
b = float(input("Елемент послідовності = "))
c = float(input("Елемент послідовності = "))
d = float(input("Елемент послідовності = "))
s = a + 2 * b + c
while d != 0:
    a = b
    b = c
    c = d
    s *= a + 2 * b + c
    d = float(input("Елемент послідовності = "))
print(s)