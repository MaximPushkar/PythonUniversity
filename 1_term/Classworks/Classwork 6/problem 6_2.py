# double all "+" and "-" in the string
s = input("string=")

t = s.split("+")
sep = "++"
print(sep.join(t))

p = sep.join(t)
t = p.split("-")
sep = "--"
print(sep.join(t))

