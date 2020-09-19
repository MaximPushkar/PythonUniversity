import math


def isprime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


n = int(input())
for i in range(n, 2 * n + 1):
    if isprime(i) and isprime(i + 2):
        print(i, i + 2)