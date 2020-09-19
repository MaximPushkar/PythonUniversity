string = input()
ans = 0
for i in string:
    try:
        ans += int(i)
    except ValueError:
        continue
print(ans)
