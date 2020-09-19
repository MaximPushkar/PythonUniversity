# scalar product of two vectors
a = list(map(float, input().split()))
b = list(map(float, input().split()))

if len(a) != len(b):
    print("nope")
else:
    c = 0
    for i in range(len(a)):
        c += a[i] * b[i]
    print(c)