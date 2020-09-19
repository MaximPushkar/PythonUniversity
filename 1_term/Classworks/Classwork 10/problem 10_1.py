"""print(set(input().split()))"""

"""a = input()
b = input()
A, B = set(a), set(b)
if A >= B:
    print(True)
else:
    print(False)"""


a = input()
b = input()

A = {}
B = {}

for i in a:
    if i not in A:
        A[i] = a.count(i)

for i in b:
    if i not in B:
        B[i] = b.count(i)

p = True
for i in B:
    if i not in A:
        p = False
        break
    elif A[i] < B[i]:
        p = False
        break

print(p)