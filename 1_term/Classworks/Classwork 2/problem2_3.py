x = float(input("x="))
if x <= 0:
    f = 0
elif 1 > x > 0:
    f = x * x
else:
    f = x ** 4
print("f=", f)