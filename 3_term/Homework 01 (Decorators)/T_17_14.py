# Нехай результатом функції f є список деяких елементів. Побудувати
# декоратор, який модифікує цей список так, щоб він не містив повторів.
# Перевірити роботу декоратора для функції, яка повертає список слів, що
# містяться у текстовому файлі.


def without_repetition(f):
    def _without_repetition(*args, **kwargs):
        return list(set(f(*args, **kwargs)))
    return _without_repetition


@without_repetition
def f(name):
    t = open(name, 'r')
    s = t.read()
    s = s.split()
    t.close()
    return s


if __name__ == '__main__':
    print(f('file.txt'))
