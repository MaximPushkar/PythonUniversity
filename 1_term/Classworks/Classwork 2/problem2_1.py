n = int(input("n="))
print(n % 2 == 0)
print(n % 10 == 0)
b = n % 10
a = n // 10
print(a + b >= 10 and 9 >= a > 0)