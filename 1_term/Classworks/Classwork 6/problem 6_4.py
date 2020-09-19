def summetr(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


s = input()
res = False
for i in range(len(s)):
    if summetr(s[:i:]) and summetr(s[i::]):
        res = True
        break
print(res)


#8993