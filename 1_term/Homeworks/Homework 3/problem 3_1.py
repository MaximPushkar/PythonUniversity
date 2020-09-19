"""n = int(input("n="))
i = 2
print(1, end="")
while i <= n:
    print(" *", i, end="")
    i += 1"""

'''n = int(input("n="))
m = int(input("m="))
s=0
for i in range(m):
    s += n
print("n * m =", s)'''

n = int(input("n="))
i = 1
r = 0
a = float(input("a="))
while i <= n:
    b = float(input("Елемент послідовності = "))
    if b == a:
        r = i
        break
    else:
        i = i + 1
print("номер:", r)
