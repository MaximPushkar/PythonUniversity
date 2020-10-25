# Скласти програму пошуку найменшого серед найбільших елементів
# рядків квадратної дійсної матриці порядку n.
# Використати масиви numpy та векторизувати програмний код.


import numpy as np


def min_max(x):
    return np.min(np.max(x, axis=1))


if __name__ == '__main__':
    x = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [-7, -8, -9]])
    print(x)
    print()

    print(min_max(x))
