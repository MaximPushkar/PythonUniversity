def P(n):
    P_0, P_1, P_2 = 1, 1, 1
    for i in range(n - 2):
        P_0, P_1, P_2 = P_1, P_2, P_0 + P_1
    return P_2


i = 10
while P(i) <= 100000:
    i += 1
print(i - 1)

