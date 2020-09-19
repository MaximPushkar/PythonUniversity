"""s = 0
p = 0
for i in range(200, 301):
    for j in range(1, i):
        if i % j == 0:
            s += j
    for t in range(1, s):
            if s % t == 0:
                p += t
        if p == i:
            print(i, s)"""

import math

'''def f(n):
    f = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            f += i
    return f'''

def f(n):
    f = 0
    for i in range(1, n):
        if n % i == 0:
            f += i
    return f


for i in range(200, 301):
    for j in range(200, i + 1):
        if f(i) == j and f(j) == i:
            print(i, j)
            if i != j:
                print(j, i)