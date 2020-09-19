n = int(input())
x = float(input())
x_n = 1
for i in range(1, n + 1):
    x_n *= (-1) * x_n * x ** 2 / (2 * i * (2 * i - 1))
print(x_n)

S_n = 0
t = - 1
for i in range(1, n + 1):
    t *= - i
    S_n += 1 / t
print(S_n)

P_n = 1
t = 1
for i in range(1, n + 1):
    t *= (i + 1)
    P_n *= 1 / t
print(P_n)

D_1 = 5
D_2 = 20
D_n = 5 * D_2 - 6 * D_1
for i in range(n - 1):
    D_1, D_2, D_n = D_2, D_n, D_1 + D_2
print(D_n)

"""D_1 = D_2
    D_2 = D_n
    D_n = D_1 + D_2"""

F_1 = 1
F_2 = 1
F = 2
for i in range(n - 3):
    F_1 = F_2
    F_2 = F
    F = F_1 + F_2
print(F)

Ans_n = 1
for i in range(1, n + 1):
    Ans_n = i + 1 / Ans_n