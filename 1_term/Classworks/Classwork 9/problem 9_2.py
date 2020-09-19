# sum of matrices, product of matrices, power of matrices
# matlib
# 4376 4752 870 1311
# output a matrix
# fractal tree
# 4751 2668 4749 2669 4376


def print_matrix(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end="  ")
        print()


def sum_of_matrices(A, B):
    ans = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            ans[i][j] = A[i][j] + B[i][j]
    return ans


def product_of_matrices(A, B):
    ans = [[0 for i in range(len(B[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            scalar_product = 0
            for t in range(len(A[0])):
                scalar_product += A[i][t] * B[t][j]
            ans[i][j] = scalar_product
    return ans


m = int(input("к-во строк первой матрицы = "))
n = int(input("к-во столбцов первой матрицы = "))
k = int(input("к-во столбцов второй матрицы = "))

A = [list(map(float, input().split())) for i in range(m)]
print()

B = [list(map(float, input().split())) for i in range(n)]
print()

# we expect, that input is correct

print_matrix(product_of_matrices(A, B))

