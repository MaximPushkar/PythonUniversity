x = float(input("x="))
y = float(input("y="))
print(x <= y <= 1 and y >= - x)
print(abs(x) <= 1 and abs(y) <= 1)
print(2 >= x >= 0 and 1 >= y >= 0)
print(x * x + y * y <= 4 and abs(x) + abs(y) >= 2)
if x >= 0 and y >= 0:
    print("no")
elif x * x + y * y >= 4 and abs(x) <= 2 and abs(y) <= 2:
    print("yes")
else:
    print("no")