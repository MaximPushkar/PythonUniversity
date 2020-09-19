def read_matrix(file):
    f = open(file, "r")
    matrix = []
    for line in f:
        numbers = line.split()
        lst = [float(i) for i in numbers]
        matrix.append(lst)
    f.close()
    return matrix


def write_matrix(matrix, file):
    f = open(file, "w")
    for i in matrix:
        for j in i:
            f.write(str(j) + " ")
        f.write('\n')
    f.close()


"""m = [[1, 1], [2, 2]]
write_matrix(m, "new.txt")"""


def summ(file_1, file_2):
    A, B = read_matrix(file_1), read_matrix(file_2)
    C = [[0 for i in range(len(A[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j]
    return C


def product(file_1, file_2):
    A, B = read_matrix(file_1), read_matrix(file_2)
    C = [[0 for i in range(len(A[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B)):
                for t in range(len(B[0])):
                    C[i][t] += A[i][j] * B[k][t]
    return C