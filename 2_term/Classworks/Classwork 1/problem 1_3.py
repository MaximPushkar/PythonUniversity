def nine(file):
    f = open(file, 'w')
    for i in range(1, 10):
        f.write(str(i) * i + '\n')
    f.close()


def print_file(file):
    f = open(file, mode='r')
    s = f.read()
    print(s)
    f.close()


nine("abc.txt")
print_file("abc.txt")
