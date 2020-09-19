n = int(input())
M = [list(map(int, input().split())) for i in range(n)]

s = 0
for i in range(n):
    s += M[i][i]

t = 0
for i in range(n):
    t += M[i][n-i-1]

print(s, t)