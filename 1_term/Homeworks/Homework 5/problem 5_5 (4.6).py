# print vector * scalar
l = list(map(float, input().split()))  # create the list
k = float(input())
s = []
for i in l:
    j = i * k
    s.append(j)
print(s)

# create the vector, parallel to the given vector with length 1
import math

q = 0
for i in l:
    q += i ** 2
q = math.sqrt(q)
t = []
for i in l:
    j = i / q
    t.append(j)
print(t)

# change the order of the vector`s components
print(l[::-1])

print("---------------------")

a = list(map(float, input().split()))
b = list(map(float, input().split()))
n = len(a) if len(a) < len(b) else len(b)
ans = []
for i in range(n):
    if a[i] == b[i]:
        ans.append(i)
print(ans)