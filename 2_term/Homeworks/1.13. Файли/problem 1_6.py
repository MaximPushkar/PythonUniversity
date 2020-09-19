# 13.5


def numbers(file):
    f = open(file, "r")
    line = f.readline()
    numbers = line.split()
    lst = [int(i) for i in numbers]
    f.close()
    return lst


def number_of_evens(file):
    num = numbers(file)
    counter = 0
    for i in num:
        if i % 2 == 0:
            counter += 1
    return counter


def number_of_squares(file):
    num = numbers(file)
    counter = 0
    for i in num:
        if (int(i ** (1 / 2))) ** 2 == i and int(i ** (1 / 2)) % 2 == 1:
            counter += 1
        elif (int(i ** (1 / 2)) + 1) ** 2 == i and int(i ** (1 / 2)) + 1 % 2 == 1:
            counter += 1
    return counter


def difference(file):
    lst_1 = [i for i in numbers(file) if i % 2 == 0]
    lst_2 = [i for i in numbers(file) if i % 2 == 1]
    return max(lst_1) - min(lst_2)


print(number_of_evens("text.txt"))
print(number_of_squares("text.txt"))
print(difference("text.txt"))
