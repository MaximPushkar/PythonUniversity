class MutableString:
    def __init__(self, string):
        if isinstance(string, MutableString):
            self.string = string.string
        elif isinstance(string, str):
            try:
                f = open(string, "r", encoding="utf-8")
                string = ""
                for line in f.readlines():
                    string += line
                self.string = list(string)
                f.close()
            except FileNotFoundError:
                self.string = list(string)
        elif isinstance(string, list):
            self.string = string

    def __str__(self) -> str:
        string = ""
        for i in self.string:
            string += i
        return string

    def __len__(self):
        return len(self.string)

    def __getitem__(self, key):
        """ Метод, що перевантажує оператор [] для читання
        :param key: Ключ
        :return: значення, що відподає ключу"""
        if key not in range(-len(self), len(self)):
            # ключ за межами рядка
            raise IndexPositiveError(IndexPositiveError.KEY_OUT_OF_RANGE, "KEY_OUT_OF_RANGE")
        if key < 0:
            # ключ від'ємний
            raise IndexPositiveError(IndexPositiveError.NEGATIVE_KEY, "NEGATIVE_KEY")
        return self.string[key]

    def __setitem__(self, key, value):
        """ Метод, що перевантажує оператор [] для запису
        :param key: Ключ
        :param value: Значення"""
        if key not in range(-len(self), len(self)):
            # ключ за межами рядка
            raise IndexPositiveError(IndexPositiveError.KEY_OUT_OF_RANGE, "KEY_OUT_OF_RANGE")
        if key < 0:
            # ключ від'ємний
            raise IndexPositiveError(IndexPositiveError.NEGATIVE_KEY, "NEGATIVE_KEY")
        self.string[key] = value

    def __add__(self, other):
        return MutableString(self.string + other.string)

    def __mul__(self, number):
        return MutableString(self.string * number)

    def __contains__(self, item):
        return item in self.string


class IndexPositiveError(IndexError):

    # Сталі для зазначення коду помилки
    KEY_OUT_OF_RANGE = 0
    NEGATIVE_KEY = 1

    def __init__(self, err_code, message):
        """ Конструктор
        :param err_code: код помилки
        :param message: повідомлення"""
        super().__init__()
        self.message = message
        self.err_code = err_code

    def __str__(self) -> str:
        return str(self.message)


# test
s = MutableString(input("string = "))
print(s[0], s[1])
# print(s[1000])
# print(s[-1])

s[0] = "q"
print(s)

# s[-1] = "w"
# s[1000] = "x"
