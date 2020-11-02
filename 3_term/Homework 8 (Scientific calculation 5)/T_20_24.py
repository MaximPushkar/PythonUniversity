# У капелюсі є m*k кульок: по k кульок m кольорів (m > 1). За один раз
# витягають d кульок (1 < d <= k). Яка ймовірність того, що всі вони одного кольору?
# Розв’язати задачу методом Монте-Карло з використанням масивів numpy.
# Векторизувати програмний код, наскільки можливо.


import numpy as np


TEST_NUM = 100000


def check(choice):
    rez = np.zeros(choice.shape[0])
    for i in range(choice.shape[0]):
        rez[i] = True
        for j in range(choice.shape[1]):
            if choice[i, j] != choice[i, 0]:
                 rez[i] = False
                 break
    return rez


def beads_probability(beads, count):
    choice = np.zeros((TEST_NUM, count))
    for i in range(TEST_NUM):
        choice[i, :] = np.random.choice(beads, count, replace=False)
    rez = check(choice)
    return np.sum(rez) / TEST_NUM


if __name__ == '__main__':

    number_of_colors = 5
    number_of_balls_for_color = 6
    count = 4

    # beads = tuple(map(int, np.kron(np.arange(1,6), np.ones(5))))

    beads = ()
    k = 0
    for i in range(number_of_colors):
        for j in range(number_of_balls_for_color):
            beads += (k,)
        k += 1

    p = beads_probability(beads, count)
    print(p)
    
    print('теоретична відповідь: ', 5/1827)
