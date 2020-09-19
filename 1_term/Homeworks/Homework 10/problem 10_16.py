n = int(input())
s = input().split()
s = set([abs(int(i)) for i in s])
print(len(s))