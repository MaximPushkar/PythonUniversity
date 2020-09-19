a = int(input("a="))  # количество строк -- а + 1
n = int(input("n="))  # количество столбцов -- n

'''for i in range(1, a + 1): # i это номер строчки, в которой мы находимся
    for j in range(1, n):   # j это номер столбца, в котором мы находимся
        print("   ", (i - 1) * n + j, "   |", end="")
    print("   ", i * n)
    for k in range(0, n - 1):
        print("-----------", end="")
    print("---------")'''


for i in range(1, a + 2): # i это номер строчки, в которой мы находимся
    for j in range(1, n):   # j это номер столбца, в котором мы находимся
        print("   ", i + j - 1, "   |", end="")
    print("   ", i + n - 1)
    for k in range(0, n - 1):
        print("-----------", end="")
    print("---------")
