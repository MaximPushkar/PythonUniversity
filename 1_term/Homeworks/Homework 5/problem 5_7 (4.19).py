n = int(input("n="))
A = [list(map(float, input("A=").split())) for i in range(n)]


def f(x):
    s = 0
    for i in range(n):
        s += A[i][x]
    return s


ans = 0
for i in range(n):
    for j in range(len(A[0])):
        if 2 * A[i][j] > f(j):
            ans += 1
print(ans)
