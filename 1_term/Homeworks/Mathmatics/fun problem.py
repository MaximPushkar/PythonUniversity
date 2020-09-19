def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n - 1)

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if 100 * i + 10 * j + k == f(i) + f(j) + f(k):
                print(i, j, k)

print("-------")

for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            for t in range(0, 10):
                if 1000 * i + 100 * j + 10 * k + t == i ** i + j ** j + k ** k + t ** t:
                    print(i, j, k, t)

# there aren`t any 2- and 3- digit numbers like that