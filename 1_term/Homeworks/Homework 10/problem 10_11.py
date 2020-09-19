def print_matrix(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end=" ")
        print()


n, m = map(int, input().split())
M = [list(map(int, input().split())) for i in range(n)]

print(m, n)

N = []
for i in range(m):
    t = []
    for j in range(n):
        t.append(M[j][i])
    t = t[::-1]
    N.append(t)

print_matrix(N)