x = float(input("x="))
y = float(input("y="))
z = float(input("z="))
if abs(y) <= abs(z) and abs(x) <= abs(z):
    M = z
elif abs(z) <= abs(x) and abs(y) <= abs(x):
    M = x
else:
    M = y
print("M=", M)
# new programme
if abs(y) >= abs(z) and abs(x) >= abs(z):
    m = z
elif abs(z) >= abs(x) and abs(y) >= abs(x):
    m = x
else:
    m = y
print("m=", m)
# new programme
if x * y >= x * z and x * y >= y * z:
    t = x * y
elif x * z >= x * y and x * z >= y * z:
    t = x * z
else:
    t = y * z
print("t=", t)
