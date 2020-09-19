import math


def is_prime(n):
    p = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p = False
            break
    return p


counter = 0
for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                if is_prime(a + b + c + d) and is_prime(d + 10 * c + 100 * b + 1000 * a):
                    counter += 1
print(counter)
