class Eq:
    def init(self, b, c):
        self.b = b
        self.c = c

    def solve(self):
        if self.b != 0:
            return (- self.c / self.b,)
        elif self.c == 0:
            return ("infinity",)
        else:
            return tuple()

    def show(self):
        if self.b != 0:
            print(self.b, "*x +", self.c)
        else:
            print(self.c)


class QuEq(Eq):
    def init(self, a, b, c):
        super().__init__(b, c)
        self.a = a

    def show(self):
        print(self.a, "*x^2 +", end='')
        super().show()

    def dis(self):
        return (self.b) ** 2 - 4 * self.a * self.c

    def solve(self):
        if self.a == 0:
            return super().solve()
        else:
            if self.dis() < 0:
                return tuple()
            elif self.dis() == 0:
                return ((- self.b) / (2 * self.a),)
            elif self.dis() > 0:
                return (
                (- self.b - self.dis() ** (1 / 2)) / (2 * self.a), ((- self.b + self.dis() ** (1 / 2)) / (2 * self.a)))


class BiQuEq(QuEq):
    def init(self, a, b, c):
        super().__init__(b, 0, c)
        self.a = a

    def show(self):
        print(self.a, "*x^4 + ", end='')
        super().show()

    def dis(self):
        return (self.b) ** 2 - 4 * self.a * self.c

    def solve(self):
        solutions = QuEq(self.a, self.b, self.c).solve()
        if len(solutions) == 0:
            return tuple()
        elif len(solutions) == 1:
            if solutions[0] > 0:
                return (solutions[0](1 / 2), - solutions[0](1 / 2))
            elif solutions[0] == 0:
                return (0,)
            else:
                return tuple()
        elif len(solutions) == 2:
            ans = tuple()
            if solutions[0] > 0:
                ans += (solutions[0](1 / 2), - solutions[0](1 / 2))
            elif solutions[0] == 0:
                ans += (0,)
            else:
                ans += tuple()

            if solutions[1] > 0:
                ans += (solutions[1](1 / 2), - solutions[1](1 / 2))
            elif solutions[1] == 0:
                ans += (0,)
            else:
                ans += tuple()

            return ans


a = BiQuEq(1, 4, -10)
a.show()
print(a.solve())

file = "qwerty.txt"
f = open(file)
counter = 0
dict = {0: [], 1: [], 2: [], 3: [], 4: [], "infinity": []}
for line in f:
    counter += 1
    coef = [float(i) for i in line.split()]
    a = BiQuEq(*coef)
    solutions = a.solve()
    i = len(solutions)
    dict[i].append(counter)

print(dict)