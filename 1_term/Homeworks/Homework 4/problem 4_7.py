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