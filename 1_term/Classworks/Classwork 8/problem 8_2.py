def around(i, j, k, t):
    if abs(i - j) <= 1 and abs(k - t) <= 1:
        return True
    return False


def construct_component(i, j):
    q = []
    if A[i][j] != 1:
        return q
    else:
        q= [[i, j]]
        for k in range(n):
            for t in range(n):
                if [k, t] not in q:
                    for qwe in q:
                        if A[k][t] == 1 and around(qwe[0], qwe[1], k, t):
                            q.append([k, t])
                            print(q)
        return q


n = int(input())
A = [list(map(int, input().split())) for i in range(n)]
B = A[::]

print(construct_component(0, 0))