# there is a string which contains some correctly writen arithmetic formula.
s = input()
# You need to count the number of arithmetic operations in it
ans = 0
i = 0
while i < len(s):
    if s[i] == "+" or s[i] == "%" or s[i] == "-":
        ans += 1
        i += 1
        continue
    elif s[i] == "*":
        if s[i + 1] == "*":
            ans += 1
            i += 2
            continue
        else:
            ans += 1
            i += 1
            continue
    elif s[i] == "/":
        if s[i + 1] == "/":
            ans += 1
            i += 2
            continue
        else:
            ans += 1
            i += 1
            continue
    else:
        i += 1
print(ans)