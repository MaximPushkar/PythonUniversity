# You need to decrypt the Caesar's cipher with the step k
s = input()
k = int(input())
l = [ord(i) - k for i in s]

for i in range(len(l)):
    j = l[i]
    if j < ord("A"):
        l[i:i+1] = chr(j + ord("Z") - ord("A") + 1)
    else:
        l[i:i + 1] = chr(j)

for j in l:
    print(j, end="")