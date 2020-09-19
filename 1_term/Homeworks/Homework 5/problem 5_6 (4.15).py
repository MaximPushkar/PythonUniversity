# create the Matrix find the sum of the elements on the main diagonal and on the not main diagonal
n = int(input("n="))
A = []
for i in range(n):
    A.append([float(input()) for j in range(n)])
s = 0
for i in range(n):
    s += A[i][i]
print(s)

t = 0
for i in range(n):
    t += A[i][n - 1 - i]
print(t)

# find the sum of the elements, which are not on the diagonals

ans = 0
for i in range(n):
    for j in range(n):
        if i != j and i != n - 1 - j:
            ans += A[i][j]
print(ans)

# find the number of the 0-s in matrix A

qwerty = 0
for i in range(n):
    for j in range(n):
        if A[i][j] == 0:
            qwerty += 1
print(qwerty)