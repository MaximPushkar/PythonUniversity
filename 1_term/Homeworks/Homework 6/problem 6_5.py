# You need to say, is the phrase sounds like a palindrome (ignore spaces)
s = input()
t = s.split()
sep = ""
l = sep.join(t)
p = True
for i in range(len(l)):
    if l[i] != l[len(l) - i - 1]:
        p = False
        break
a = "YES" if p else "NO"
print(a)

