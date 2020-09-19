import math
x1 = float(input("x0="))
y1 = float(input("y0="))
x2 = float(input("x1="))
y2 = float(input("y1="))
x3 = float(input("x2="))
y3 = float(input("y2="))
x = float(input("x="))
y = float(input("y="))

"""a = ((x - x0) / (y - y0) - (x1 - x0) / (y1 - y0))
b = ((x - x1) / (y - y1) - (x2 - x1) / (y2 - y1))
c = ((x - x2) / (y - y2) - (x0 - x2) / (y0 - y2))
print(a / abs(a) == b / abs(b) and a / abs(a) == c / abs(c))"""

s123 = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
s12x = abs((x2 - x1) * (y - y1) - (x - x1) * (y2 - y1)) / 2
s1x3 = abs((x - x1) * (y3 - y1) - (x3 - x1) * (y - y1)) / 2
sx23 = abs((x2 - x) * (y3 - y) - (x3 - x) * (y2 - y)) / 2
print(s123 == s12x + sx23 + s1x3)
