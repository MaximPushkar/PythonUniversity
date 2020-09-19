import math


def f(x):
    return x


def C(n, k):
    if n == 1 or k == 0 or k == n:
        return 1
    else:
        return C(n-1, k-1) + C(n-1, k)


def Bernstein_polinomial_component(f, n, k, x):
    return C(n, k) * f(k / n) * x ** k * (1 - x) ** (n - k)


def Bernstein_polinomial(f, n, x):
    s = 0
    for k in range(n + 1):
        s += Bernstein_polinomial_component(f, n, k, x)


def max_of_function(f, eps):
    i = 1
    ans = abs(f(0))
    while i * eps <= 1:
        ans = abs(f(i * eps)) if abs(f(i * eps)) > ans else ans
    ans = max(ans, abs(f(1)))
    return ans
