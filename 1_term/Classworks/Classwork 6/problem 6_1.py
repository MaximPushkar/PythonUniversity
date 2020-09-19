# for i in range(ord("A"), ord("Z") + 1):
#    print(chr(i), end="")

# are the symbols "(" and ")" in the given string placed correctly
s = input("string=")
bef = 0
aft = 0
p = True
for i in s:
    if i == "(":
        bef += 1
    elif i == ")":
        aft += 1
        if aft > bef:
            p = False
            break
if bef != aft:
    p = False
print(p)