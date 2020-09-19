def number_of_empty(file):
    f = open(file)
    n = 0
    for line in f.readlines(): # or in f
        if line == "\n":
            n += 1
    f.close()
    return n


print(number_of_empty("abc.txt"))
