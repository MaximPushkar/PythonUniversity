import cmath

a = float(input("re="))
b = float(input("im="))
z = complex(a, b)
z1 = z.conjugate()
y = z ** 5 + z1 ** 2 - 1
print("y=", y)
