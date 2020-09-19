def numbers(file):
    f = open(file, "r")
    line = f.readline()
    numbers = line.split()
    lst = [float(i) for i in numbers]
    f.close()
    return lst


def summ(file):
    num = numbers(file)
    sum = 0
    for i in num:
        sum += i
    return sum


def number_of_negative(file):
    num = numbers(file)
    counter = 0
    for i in num:
        if i < 0:
            counter += 1
    return counter


def the_last(file):
    num = numbers(file)
    print(num[-1])


def maximum(file):
    num = numbers(file)
    return max(num)


def minimum(file):
    num = numbers(file)
    new_num = []
    for i in range(len(num)):
        if i % 2 == 0:
            new_num.append(num[i])
    return num
