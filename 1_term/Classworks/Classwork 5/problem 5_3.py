# derivative of the polinom in the point x
P = list(map(float, input("P=").split()))
x = float(input("x="))
d = 0
n = len(P)
for i in range(1, len(P)):
    d += P[i - 1] * (n - i) * (x ** (n - i - 1))
print(d)

# integrate P from a to b
a = float(input("a="))
b = float(input("b="))
c = 0
for i in range(1, len(P)):
    c += (P[i - 1] / (n - i + 1)) * (b ** (n - i + 1)) - (P[i - 1] / (n - i + 1)) * (a ** (n - i + 1))
print(c)