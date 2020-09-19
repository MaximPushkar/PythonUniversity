# \sum_(k=1)^(n) (a_k / b_k)^k -- ?
# a_k = a_(k-2) + b_k / 2,  a_0 = 1, a_1 = 2
# b_k = b_(k-2)^2 - a_(k-1),  b_0 = b_1 = 5


def recurrently(k):
    """ Знаходження елементів послідовностей а та b, використовуючи
            рекурентні співвідношення
        :param k: Номер члена послідовності сум, що необхідно знайти
        :return:  Знайдений член послідовності сум. """
    a_0, a_1, b_0, b_1 = 0, 2, 5, 5
    sum = (a_1 / b_1)
    for i in range(2, k + 1):
        a_0, a_1, b_0, b_1 = a_1, a_0 + (b_0 ** 2 - a_1) / 2, b_1, b_0 ** 2 - a_1
        sum += (a_1 / b_1) ** i
    return sum


def generator(k):
    """ Генератор """
    a_0, a_1, b_0, b_1 = 0, 2, 5, 5
    sum = (a_1 / b_1)
    yield sum
    for i in range(2, k + 1):
        a_0, a_1, b_0, b_1 = a_1, a_0 + (b_0 ** 2 - a_1) / 2, b_1, b_0 ** 2 - a_1
        sum += (a_1 / b_1) ** i
        yield sum


# Головна програма
n = int(input("n = "))
print()
print(recurrently(n))
print()
for el in generator(n):
    print(el)
