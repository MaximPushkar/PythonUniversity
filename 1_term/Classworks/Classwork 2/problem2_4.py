n = int(input("n="))
c = n % 10
n = (n - c) // 10
b = n % 10
n = (n - b) // 10
a = n % 10
n = (n - a) // 10
print(a == 2 or b == 2 or c == 2)
print(a % 2 == 0 and b % 2 == 0 and c % 2 == 0)
print(a + b + c == 18)