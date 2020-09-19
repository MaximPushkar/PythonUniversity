import time


def numbers(file):
    f = open(file, "r")
    line = f.readline()
    num = line.split()
    lst = [int(i) for i in num]
    f.close()
    return lst


def to_bin(n):
    lst = []
    while n != 0:
        lst.append(n % 2)
        n //= 2
    return lst[::-1]


# longest increasing subsequence version 1
def stupid(file):
    num = numbers(file)
    len_max = 0
    ans = []
    positions = []
    for i in range(0, 2 ** (len(num))):
        t = to_bin(i)
        # print("bin  ", t)
        lst = []
        for j in range(len(t[::-1])):
            if t[::-1][j] == 1:
                lst.append(num[-1 - j])
        lst = lst[::-1]
        # print("lst  ", lst)
        check = True
        for j in range(len(lst) - 1):
            if lst[j] >= lst[j + 1]:
                check = False
                break
        if check:
            if len(lst) > len_max:
                len_max = len(lst)
                ans = len(lst)
                positions = t
    return len_max, ans, positions


# well known algorithm
"""def clever(file):
    a = numbers(file)
    # create a list, which contains maximal len of increasing subsequence, ends exactly in position i
    d = [[1, [a[0]]]]
    for i in range(1, len(a)):
        maximum = 1
        t = [a[i]]
        for j in range(i - 1):
            if a[j] < a[i]:
                if maximum < d[j][0] + 1:
                    maximum = d[j][0] + 1
                    # t = d[j][1].append(a[i])
        d.append([maximum, t])
    # finding maximum of list d
    q = [i[0] for i in d]
    maxi = max(q)
    ind = q.index(maxi)
    return d[ind]"""


def clever_len(file):
    a = numbers(file)
    # create a list, which contains maximal len of increasing subsequence, ends exactly in position i
    d = [1]
    for i in range(1, len(a)):
        local_maximum = 1
        for j in range(i):
            if a[j] < a[i]:
                if local_maximum < d[j] + 1:
                    local_maximum = d[j] + 1
        d.append(local_maximum)
    # finding maximum of list d
    maxi = max(d)
    return maxi


ti = time.time()
print("len of maximal increasing subsequence:  ", clever_len("text.txt"))
print("time:  ", time.time() - ti)
print()
ti = time.time()
a = stupid("text.txt")
print("result of stupid algorithm:")
print(a)
print("time:  ", time.time() - ti)
