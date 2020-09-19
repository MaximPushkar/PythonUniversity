def polin(x):
    for i in range(len(x)):
        if x[i] != x[len(x) - i - 1]:
            return False
    return True


s = input()

sep = " "
q = sep.join(s.split(","))
w = sep.join(q.split(";"))
e = sep.join(w.split("!"))
r = sep.join(e.split("?"))
t = sep.join(r.split("."))
y = sep.join(t.split(":"))
u = sep.join(y.split("-"))
i = sep.join(u.split("("))
o = sep.join(i.split(")"))
p = sep.join(o.split("\""))
l = sep.join(p.split("\'"))
re = l.split()
print(re)

ans = -1
lenmax = 0
for i in range(len(re)):
    if len(re[i]) > lenmax and polin(re[i]):
        ans = i
        lenmax = len(re[i])
print(ans + 1)
