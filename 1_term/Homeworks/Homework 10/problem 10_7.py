def res_perm(k):
    res = []
    perm([], k, res)
    return res


def perm(l, k, res):
    if len(k) == 1:
        res.append(l + k)
    else:
        for i in range(len(k)):
            perm(l + [k[i]], k[0:i] + k[i + 1:], res)


d = res_perm(list(range(1, int(input()) + 1)))

for permutation in d:
    for el in permutation:
        print(el, end=' ')
    print()
