x = float(input())
eps = float(input())
counter = 2
a_n = x
s_n = 1 + x
while abs(a_n) >= eps:
    a_n *= x / counter
    counter += 1
    s_n += a_n
print(counter)
