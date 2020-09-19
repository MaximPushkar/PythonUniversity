n = int(input("n="))
c = n % 10
n = (n - c) // 10
b = n % 10
n = (n - b) // 10
a = n % 10
n = (n - a) // 10
x = 100 * b + 10 * c + a
print("x=", x)