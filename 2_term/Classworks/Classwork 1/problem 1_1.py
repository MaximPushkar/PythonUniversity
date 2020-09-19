def print_file(file):
    f = open(file, mode='r')
    s = f.read()
    print(s)
    f.close()


def new_read(file):
    with open(file) as f:
        while True:
            line = f.readline()
            if len(line) >= 6:
                print(line)
            elif not line:
                break


# print_file("abc.txt")
print(input()[2::])