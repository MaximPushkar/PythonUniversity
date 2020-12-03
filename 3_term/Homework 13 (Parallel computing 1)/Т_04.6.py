"""
Описати програму з графічним інтерфейсом, у якому користувач
вводить номер ціле число, а програма викликає функцію що перевіряє, чи є це
число простим. Функція має виконуватись у окремому потоці. Після
завершення обчислень результат має бути показаний також у графічному
інтерфейсі.
Графічний інтерфейс має породжувати нове вікно для кожного введеного
простого числа і в цьому вікні показувати результат після завершення
обчислень.
"""

import tkinter as tk
from concurrent.futures import ThreadPoolExecutor


def is_prime(n):
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


class PrimeSubGUI:

    def __init__(self, n):
        self._top = tk.Toplevel()
        self._top.minsize(300, 100)

        lbl = tk.Label(self._top,
                       text="is_prime({})=...".format(n),
                       font=("Arial", 24))
        lbl.pack()
        btn = tk.Button(self._top,
                        text="Закрити",
                        font=("Arial", 24),
                        command=self._top.destroy)
        btn.pack()

        result = is_prime(n)
        lbl.configure(text="is_prime({})={}".format(n, result))


class PrimeMainGUI:

    def __init__(self):
        self._top = tk.Tk()
        self._executor = ThreadPoolExecutor(max_workers=2)

        self._var = tk.IntVar(self._top, 10)
        self._make_widgets()
        self._top.mainloop()

    def _make_widgets(self):
        self._top.title("Дослідження на простоту")
        self._top.minsize(400, 200)

        ent = tk.Entry(self._top,
                       font=("Arial", 24),
                       textvariable=self._var)
        ent.pack()
        btn = tk.Button(self._top,
                        text="Дослідити",
                        font=("Arial", 24),
                        command=self._button_handler)
        btn.pack()
        btn = tk.Button(self._top,
                        text="Закрити",
                        font=("Arial", 24),
                        command=self._top.quit)
        btn.pack()

    def _button_handler(self):
        n = self._var.get()
        self._executor.submit(PrimeSubGUI, n)


if __name__ == '__main__':
    PrimeMainGUI()
