# Є список адрес заборонених сайтів.
# Інформація – у вигляді великого текстового файлу, у якому, зокрема, є трійки:
# <адреса комп’ютера> <відвіданий сайт> <дата та час>
# <адреса комп’ютера> - рядок у форматі XXX.XXX.XXX.XXX, де X – цифри (між крапками може бути й менше 3 цифр.
# <відвіданий сайт> - рядок у форматі http:// <адреса сайту>
# <дата та час> - рядок у форматі dd.mm.yyyy hh:mm:ss
# У Вас є список співробітників разом з адресами їх комп’ютерів.
# Вам потрібно підготувати звіт щодо відвідування співробітниками
# заборонених сайтів, впорядкувавши його за кількістю відвідувань.


import re

BAD = ['http://badsite.com', 'http://hell.com', 'http://qwertyASGDUFVYGABSDKJXV']

Computer_address = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
Name = r'\b[^\d\.\n]+\b'
Site_link = r'\bhttp:\/\/[^\s]+\b'
Date_time = r'\b\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}\b'


def dct_workers(file):
    with open(file, "r", encoding="utf-8") as inp:
        text = inp.read()
        rgx = re.compile(Computer_address)
        lst_1 = rgx.findall(text)
        rgx = re.compile(Name)
        lst_2 = rgx.findall(text)
        dct = dict.fromkeys(lst_1)
        for i in range(len(lst_1)):
            dct[lst_1[i]] = lst_2[i]
        return dct


def find_bad_sites(file):
    with open(file, "r", encoding="utf-8") as inp:
        text = inp.read()
        rgx_1 = re.compile(Site_link)
        rgx_2 = re.compile(Computer_address)
        rgx_3 = re.compile(Date_time)
        lst_1 = rgx_1.findall(text)
        text = text.split('\n')
        lst_2 = []
        counter = 0
        for site in lst_1:
            if site in BAD:
                lst_2.append([site, rgx_2.findall(text[counter])[0], rgx_3.findall(text[counter])[0]])
            counter += 1
        return lst_2


def _get_names(dct, lst):
    for lst_1 in lst:
        lst_1.append(dct[lst_1[1]])
    return lst


def get_names(file_1, file_2):
    return _get_names(dct_workers(file_1), find_bad_sites(file_2))


def sort_data(file_1, file_2):
    lst = get_names(file_1, file_2)
    lst_names = [i[3] for i in lst]
    dct = {}
    for name in lst_names:
        dct[name] = lst_names.count(name)
    dct = {k: v for k, v in sorted(dct.items(), key=lambda item: item[1], reverse=True)}
    return dct


def good_representation(file_1, file_2):
    dct = sort_data(file_1, file_2)
    to_write_list = []
    counter = 1
    for name in dct.keys():
        s = str(counter) + ') ' + name + '; ' + str(dct[name]) + ' порушень'
        for event in get_names(file_1, file_2):
            if event[3] == name:
                s += ';  ' + event[0] + ', ' + event[2]
        to_write_list.append(s)
        counter += 1
    return to_write_list


def write_to_file(file_1, file_2, file_to):
    lst = good_representation(file_1, file_2)
    with open(file_to, "w", encoding="utf-8") as out:
        for s in lst:
            out.write(s + '\n')


if __name__ == '__main__':
    """with open("Site_visited.txt", "r", encoding="utf-8") as inp:
        s = inp.read()
        s = change_dates(s)
    with open("output.txt", "w", encoding="utf-8") as out:
        out.write(s)"""

    # print(dct_workers("Workers_list.txt"))
    # print(find_bad_sites("Site_visited.txt"))
    # print(get_names("Workers_list.txt", "Site_visited.txt"))
    # print(sort_data("Workers_list.txt", "Site_visited.txt"))
    # print(good_representation("Workers_list.txt", "Site_visited.txt"))
    write_to_file("Workers_list.txt", "Site_visited.txt", 'Result.txt')
