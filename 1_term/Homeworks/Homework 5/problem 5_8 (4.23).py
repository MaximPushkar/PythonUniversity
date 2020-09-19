# find the number of points, which are the biggest in the line (string), but the smallest in the column (saddle point)
n = int(input("n="))
A = [list(map(float, input("A=").split())) for i in range(n)]


def f(i, j):
    p = True
    for x in range(n):
        if A[x][j] > A[i][j]:
            p = False
            break
    if p:
        for y in range(len(A[0])):
            if A[i][y] < A[i][j]:
                p = False
                break
    return p


s = []
for i in range(n):
    for j in range(len(A[0])):
        if f(i, j):
            s.append([i, j])
print(s)
print(len(s))
