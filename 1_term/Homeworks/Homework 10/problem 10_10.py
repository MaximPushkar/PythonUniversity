n, m = map(int, input().split())
A = []
for i in range(n + 1):
    t = list(map(int, input().split()))
    A.append(t)
A.pop()

B = []
for i in range(n):
    t = list(map(int, input().split()))
    B.append(t)

ans = 0
for i in range(n):
    for j in range(m):
        ans += A[i][j] * B[i][j]
print(ans)