s = input()

sep = ''
sep1 = '1'
sep3 = '3'
sep5 = '5'
sep7 = '7'
sep9 = '9'
s = sep.join(s.split(sep1))
s = sep.join(s.split(sep3))
s = sep.join(s.split(sep5))
s = sep.join(s.split(sep7))
s = sep.join(s.split(sep9))
print(s)