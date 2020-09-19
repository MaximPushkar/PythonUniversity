n = int(input())
l1 = 'a'
l2 = 'bc'
print(l1)
print(l2)
for i in range(10):
    l = l1 + l2
    l2 = l1
    l1 = l
    print(l)