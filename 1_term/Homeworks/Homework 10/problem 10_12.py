def helping_print_matrix(M):
    for i in range(len(M)):
        print(M[i][0], end="")


def beautiful_print_matrix(M):
    for i in range(len(M)):
        print(" ", end="")
        for j in range(len(M[i])):
            helping_print_matrix(M[i][j])
            print(" ", end="")
        print(" ")


def find_max_len_and_fix(l):
    ans = 0
    for i in range(len(l)):
        ans = len(l[i]) if len(l[i]) > ans else ans
    s = []
    for i in l:
        j = i[::-1]
        while len(j) < ans:
            j.append(" ")
        j = j[::-1]
        s.append(j)
    return [s, ans]


n = int(input())
M = [[(i + 1) * (j + 1) for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        M[i][j] = str(M[i][j])
        M[i][j] = list(M[i][j])

N = []
for i in range(n):
    N.append(find_max_len_and_fix(M[i])[0])

K = []
for i in range(n):
    t = []
    for j in range(n):
        t.append(N[j][i])
    K.append(t)

beautiful_print_matrix(K)