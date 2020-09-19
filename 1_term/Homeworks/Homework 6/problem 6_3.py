"""s = input()
t = [ord(i) for i in s]
ans = []
for i in range(len(s)):
    if t:
        temp = min(t)
        image = chr(temp)
        ans.append(image)
        num = t.index(temp)
        t[num : num + 1] = []
    else:
        break
print(ans)"""

s = input()
t = [ord(i) for i in s]
for i in range(len(s)):
    if t:
        temp = min(t)
        image = chr(temp)
        print(image, end="")
        num = t.index(temp)
        t[num:num + 1] = []
    else:
        break
