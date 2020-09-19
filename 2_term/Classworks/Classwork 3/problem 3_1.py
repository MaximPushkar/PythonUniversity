class QuadraticEquation:
    count = 0

    @staticmethod
    def get_count():
        return QuadraticEquation.count

    def __init__(self, a, b=0, c=0):
        if isinstance(a, QuadraticEquation):
            self._a = a._a
            self._b = a._b
            self._c = a._c
        else:
            assert a != 0
            self._a = a
            self._b = b
            self._c = c
        print("object ", self, " created")
        QuadraticEquation.count += 1

    def __del__(self):
        print("object", self, "destroyed")

    def get_view(self):
        view = "{}x^2 + {}x + {}".format(self._a, self._b, self._c)
        print(view)

    def get_dis(self):
        return self._b ** 2 - 4 * self._a * self._c

    def get_solutions(self):
        d = self.get_dis()
        if d >= 0:
            return (-self._b - d**(1/2))/(2*self._a), (-self._b + d**(1/2))/(2*self._a)
        else:
            print("equation has no real solutions")


eq = QuadraticEquation(1, -2, 0)
eq.get_view()
print(eq.get_dis())
print(eq.get_solutions())
print(QuadraticEquation.get_count())
del eq
