import math
# x0 = float(input("x0=")) ; y0 = float(input("y0="))
a = float(input("a=")) ; b = float(input("b=")) ; c = float(input("c="))
'''d = abs(a * x0 + b * y0 + c) / math.sqrt(a ** 2 + b ** 2)
print("d=", d)'''

x1 = (- b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
x2 = (- b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
print(x1, x2)