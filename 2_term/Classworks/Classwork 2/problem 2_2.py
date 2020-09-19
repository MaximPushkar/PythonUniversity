print("file {} {}".format(3, 'h'))


def read_file(file):
    try:
        f = open(file)
        for line in f:
            print(line, end="")
    except FileNotFoundError:
        print("This file does not exist")
    except PermissionError:
        print("You have not such rights to open this file ")
    except IOError:
        print("I can not open this file")


print("file {:.2f} {}".format(3.141592653587, 'h'))