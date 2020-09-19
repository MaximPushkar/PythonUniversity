n = int(input())

inp = []
for i in range(n):
    inp.append("".join(input().split(":")).split())

for i in range(n):
    inp[i] = inp[i][:len(inp[i]) - 1]

print(inp)

maximal = 0
for i in range(n):
    maximal = max(maximal, len(inp[i]))

for i in range(n):
    t = [inp[i][0]]
    inp[i][0:1] = []
    while len(inp[i]) != maximal:
        inp[i].append("middle")
    inp[i][0:1] = t

print(inp)

"inp[i] = inp[i][::-1]"


new_list = [[] for i in range(n)]
for i in range(n):
    t = ""
    for j in range(1, len(inp[i])):
        if inp[i][j] == "upper":
            t += "2"
        if inp[i][j] == "middle":
            t += "1"
        else:
            t += "0"
    new_list[i] = [t, inp[i][0]]

print(new_list)



