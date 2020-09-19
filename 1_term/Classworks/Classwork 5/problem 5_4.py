# create the Matrix and transpose it
n = int(input("n="))
A = [list(map(float, input("A=").split())) for i in range(n)]
B = [[0 for x in range(n)] for y in range(len(A[0]))]

for i in range(len(A[0])):
    for j in range(n):
        B[i][j] = A[j][i]
print(B)


# 4.21e + photo
