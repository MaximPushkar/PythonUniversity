import math


def func_1(x, k):
    ans = 1
    for i in range(1, k + 1):
        ans *= x * (i + 1) / i ** 2
    return ans


def func_2(n):
    ans = 0
    t = - 1
    for i in range(2, n + 1):
        t *= - 1
        ans += t * (i - 1) / i
    return ans


def is_prime(q):
    ans = True
    for i in range(2, int(math.sqrt(q)) + 1):
        if q % i == 0:
            ans = False
            break
    return ans


def F_n(n):
    F_2 = 1
    F_n = 1
    for i in range(n - 2):
        F_2, F_n = F_n, F_n + F_2
    return F_n


def func_3(n):
    ans = True
    for i in range(5, n + 1):
        if is_prime(F_n(i)) and not is_prime(i):
            ans = False
            break
    return ans


def determinant(a, b, n):
    D_1 = a + b
    D_2 = a ** 2 + b ** 2 + a * b
    for i in range(n - 2):
        D_1, D_2 = D_2, (a + b) * D_2 - a * b * D_1
    return D_2


def P(n):
    P0, P1, P2 = 1, 1, 1
    for i in range(n - 3):
        P0, P1, P2 = P1, P2, P1 + P0
    return P2


def func_4(n):
    ans = True
    for i in range(15, n + 1):
        if P(i) != 4 * P(i - 5) + P(i - 14):
            ans = False
            break
    return ans


def func_5(n):
    a_1, a_2, b_1, b_2 = 0, 1, 1, 1
    t = 4
    s_n = 4
    for i in range(3, n + 1):
        t *= 2
        b_1, b_2 = b_2, b_2 + a_2
        a_1, a_2 = a_2, a_2 / i + a_1 * b_2
        s_n += t / (a_2 + b_2)
    return s_n