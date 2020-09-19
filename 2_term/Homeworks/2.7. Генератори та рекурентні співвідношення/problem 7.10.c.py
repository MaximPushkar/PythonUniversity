# D_n = 2D_(n-1) - D_(n-2), D_1 = 2, D_2 = 3


def recurrently(k):
    """ Знаходження елементів послідовності використовуючи
            рекурентні співвідношення
        :param k: Номер члена послідовності, що необхідно знайти
        :return:  Знайдений член послідовності. """
    D_1, D_2 = 2, 3  # початкове значення
    if k == 1:
        return D_1
    elif k == 2:
        return D_2
    else:
        for i in range(3, k + 1):
            D_1, D_2 = D_2, 2 * D_2 - D_1
        return D_2


def generator(k):
    """ Генератор """
    D_1, D_2 = 2, 3  # початкове значення
    yield D_1
    yield D_2
    for i in range(3, k + 1):
        yield 2 * D_2 - D_1  # повертаємо поточний член послідовності
        D_1, D_2 = D_2, 2 * D_2 - D_1


# зауваження: з рекурентного співвфдношення та початкових умов легко бачити, що D_n = n + 1.


# Головна програма
n = int(input("n = "))
print()
print(recurrently(n))
print()
for el in generator(n):
    print(el)
