def polin(x):
    if x == x[::-1]:
        return True
    return False


s = input()
p = True
for i in range(len(s)):
    t = [j for j in s]
    t[i:i + 1] = []
    if polin(t):
        print("yes")
        for j in t:
            print(j, end="")
        p = False
        break
if p:
    print("no")
