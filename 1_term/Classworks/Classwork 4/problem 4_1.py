n = int(input("n="))
maxim = float(input("a_0="))     #max(a_i)
ans = - maxim     #max(-1**n * a_i)
for i in range(n - 1):
    a = float(input("a_{}=".format(i + 1)))
    maxim = a if a > maxim else maxim
    ans = (- 1) ** i * a if (- 1) ** i * a > ans else ans
print(maxim)
print(ans)


