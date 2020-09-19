# ??????????????????????????????????????????
s = input("enter your code:")

ans = 0

q = False
w = False
e = False
r = False
t = False
for i in s:
    if ord("z") >= ord(i) >= ord("a"):
        q = True
    elif ord("Z") >= ord(i) >= ord("A"):
        w = True
    elif ord("9") >= ord(i) >= ord("0"):
        e = True
    elif ord("+") >= ord(i) >= ord("!"):
        r = True

n = len("".join(s.split()))
if n >= 8:
    t = True
ans += q + w + e + r + t
print(ans)