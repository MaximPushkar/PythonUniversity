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

    def __str__(self):
        string = ""
        for i in self.string:
            string += i
        return string

    def __len__(self):
        return len(self.string)

    def __getitem__(self, key):
        return self.string[key]

    def __add__(self, other):
        return MutableString(self.string + other.string)

    def __mul__(self, number):
        return MutableString(self.string * number)

    def __contains__(self, item):
        return item in self.string


class MutableStringIterator:
    """ Ітератор для класу MutableString """

    def __init__(self, collection):
        """ Конструктор ітератора
        :param collection: посилання на колекцію
        """
        self._list_of_symbols = collection.string
        self._cursor = 0  # поточна позиція ітератора у колекції

    def __next__(self):
        try:
            symbol = self._list_of_symbols[self._cursor]
            self._cursor += 1
            return symbol
        except IndexError:
            raise StopIteration


def from_eng_to_ukr(symbol):
    global counter
    if symbol == "e":
        symbol = "е"
        counter += 1
    elif symbol == "y":
        symbol = "у"
        counter += 1
    elif symbol == "i":
        symbol = "і"
        counter += 1
    elif symbol == "p":
        symbol = "р"
        counter += 1
    elif symbol == "a":
        symbol = "а"
        counter += 1
    elif symbol == "x":
        symbol = "х"
        counter += 1
    elif symbol == "c":
        symbol = "с"
        counter += 1
    elif symbol == "o":
        symbol = "о"
        counter += 1
    return symbol


# test
""" s = MutableString("12345678901123ksJC")
for el in s:
    print(el)"""


# problem
file = "text.txt"
new_file = "new text.txt"
r = MutableString(file)
counter = 0
for el in r:
    el = from_eng_to_ukr(el)
    f = open(new_file, "a", encoding="utf-8")
    f.write(el)
    f.close()
print(counter)
