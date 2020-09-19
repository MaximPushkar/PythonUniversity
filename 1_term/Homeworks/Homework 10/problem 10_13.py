def print_matrix(M):
    print(" ", end="")
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end=" ")
        print()


def find_max_len_and_fix(l):
    ans = 0
    for i in range(len(l)):
        ans = len(l[i]) if len(l[i]) > ans else ans
    s = []
    for i in l:
        j = i
        while len(j) < ans:
            j = " " + j
        s.append(j)
    return [s, ans]


n = int(input())
M = [[(i + 1) * (j + 1) for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        M[i][j] = str(M[i][j])

N = []
for i in range(n):
    N.append(find_max_len_and_fix(M[i])[0])

K = []
for i in range(n):
    t = []
    for j in range(n):
        t.append(N[j][i])
    K.append(t)

print_matrix(K)
