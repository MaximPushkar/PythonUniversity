try:
    f = open("content.txt")
except FileNotFoundError:
    print("File \"content.txt\" does not exist")
except PermissionError:
    print("You have not such rights to open file \"content.txt\"")
except IOError:
    print("This program can\'t open file \"content.txt\"")
else:
    p = True
    s = 0
    for line in f:
        line = line[:-1]
        try:
            t = open(line)
        except FileNotFoundError:
            print("file {} doesn\'t exist".format(line))
            p = False
        except PermissionError:
            print("You have not such rights to open file {}".format(line))
            p = False
        except IOError:
            print("This program can\'t open file {}".format(line))
            p = False
        else:
            new_line = t.readline()
            new_line = new_line.split()
            try:
                new_list = [float(i) for i in new_line]
            except ValueError:
                print("file {} contains not only float".format(line))
                p = False
            else:
                for i in new_list:
                    s += i
                t.close()
            if not p:
                break
    if p:
        print("sum = ", s)
