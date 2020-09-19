n = int(input())

def f(n):
    f = 0
    for i in range(1, n):
        if n % i == 0:
            f += i
    return f

if f(n) == n:
    print("yes")
else:
    print("no")

"""for i in range(1, n + 1, 1):
    if f(i) == i:
        print(i)"""