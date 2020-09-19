# how many elements are greater than 0
l = list(map(float, input().split()))
a = 0
b = 0
for i in l:
    if i >= 0:
        a += 1
    if i <= 0:
        b += 1
if a > b:
    print("number of positive is bigger than number of negative")
elif a < b:
    print("number of negative is bigger than number of positive")
else:
    print("number of negative is equal to number of positive")


