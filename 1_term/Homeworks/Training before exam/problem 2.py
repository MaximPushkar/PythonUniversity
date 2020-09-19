s = input()
n = 7
ans = ""
for i in s:
    if ord("Z") >= ord(i) >= ord("A"):
        i = chr(ord(i) - (ord("A") - ord("a")))
        if ord(i) + 7 <= ord('z'):
            i = chr(ord(i) + 7)
        else:
            i = chr(ord(i) + 6 - ord("z") + ord("a"))
    elif ord("z") >= ord(i) >= ord("a"):
        if ord(i) + 7 <= ord('z'):
            i = chr(ord(i) + 7)
        else:
            i = chr(ord(i) + 6 - ord("z") + ord("a"))
    elif i == " ":
        i = "*"
    ans += i
print(ans)
