class MutableString:
    def __init__(self, string):
        if isinstance(string, MutableString):
            self.string = string.string
        elif isinstance(string, str):
            try:
                file = open(string, "r", encoding="utf-8")
                string = ""
                for line in file.readlines():
                    string += line
                self.string = list(string)
                file.close()
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

    def from_eng_to_ukr(self):
        counter = 0
        for position in range(len(self.string)):
            if self.string[position] == "e":
                self.string[position] = "е"
                counter += 1
            elif self.string[position] == "y":
                self.string[position] = "у"
                counter += 1
            elif self.string[position] == "i":
                self.string[position] = "і"
                counter += 1
            elif self.string[position] == "p":
                self.string[position] = "р"
                counter += 1
            elif self.string[position] == "a":
                self.string[position] = "а"
                counter += 1
            elif self.string[position] == "x":
                self.string[position] = "х"
                counter += 1
            elif self.string[position] == "c":
                self.string[position] = "с"
                counter += 1
            elif self.string[position] == "o":
                self.string[position] = "о"
                counter += 1
        return counter

    def write_in_file(self, file):
        new_file = open(file, "w", encoding="utf-8")
        new_file.write(self.__str__())
        new_file.close()


# test
"""s = MutableString("123 456 q")
t = MutableString(s)
v = MutableString(["1", "4", " ", "5"])
p = MutableString("text.txt")

print(s, t, v, p)
print(len(s), len(t), len(v), len(p))
print(s[0], t[3], v[1], p[0])
print(s + v)
print(v * 3)
print("1" in s, "3" in v)"""


# problem
r = MutableString("text.txt")
number_of_corrections = r.from_eng_to_ukr()
r.write_in_file("new text.txt")
print(number_of_corrections)

