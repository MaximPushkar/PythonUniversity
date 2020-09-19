class Polynomial:
    count = 0

    @staticmethod
    def get_count():
        return Polynomial.count

    def __init__(self, coefficients):
        if isinstance(coefficients, str):
            try:
                self.coefficients = [float(i) for i in coefficients.split()]
            except ValueError:
                f = open(coefficients, "r")
                line = f.readline()
                self.coefficients = [float(i) for i in line.split()]
        elif isinstance(coefficients, Polynomial):
            self.coefficients = coefficients.coefficients
        else:
            self.coefficients = coefficients
        Polynomial.count += 1

    def get_view(self):
        view = ""
        for i in range(len(self.coefficients)):
            if self.coefficients[i] == 0:
                continue
            elif i == 0:
                view += str(self.coefficients[0]) + " * x^{} ".format(len(self.coefficients) - 1)
            elif len(self.coefficients) - i - 1 == 1:
                view += "+ " + str(self.coefficients[i]) + " * x "
            elif len(self.coefficients) - i - 1 == 0:
                view += "+ " + str(self.coefficients[i])
            else:
                view += "+ " + str(self.coefficients[i]) + " * x^{} ".format(len(self.coefficients) - i - 1)
        if len(view) == 0:
            print(0)
        else:
            while view[0] == " " or view[0] == "+":
                view = view[1::]
            print(view)

    def get_value(self, x):
        value = 0
        for i in range(len(self.coefficients)):
            value += self.coefficients[i] * x ** (len(self.coefficients) - i - 1)
        return value

    def derivative(self):
        new_coefficients = [self.coefficients[i] * (len(self.coefficients) - i - 1) for i in
                            range(len(self.coefficients) - 1)]
        return Polynomial(new_coefficients)

    def sum(self, other):
        if len(self.coefficients) < len(other.coefficients):
            other, self = self, other
        coeffs = other.coefficients[::-1]
        while len(coeffs) < len(self.coefficients):
            coeffs.append(0)
        coeffs = coeffs[::-1]
        # coeffs = [x + y for x, y in itertools.izip_longest(self.coeffs, other.coeffs, fillvalue=0)]
        new_coefficients = [self.coefficients[i] + coeffs[i] for i in range(len(self.coefficients))]
        return Polynomial(new_coefficients)

    def scale(self, a):
        return Polynomial([i * a for i in self.coefficients])

    def difference(self, other):
        return self.sum(other.scale(-1))

    def product(self, other):
        new_coefficients = [0 for i in range(len(self.coefficients) + len(other.coefficients))]
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                new_coefficients[i + j + 1] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(new_coefficients)

    def power(self, n):
        ans = Polynomial([1])
        for i in range(n):
            ans = self.product(ans)
        return ans

    def composition(self, other):
        # put other into self
        ans = Polynomial([0])
        for i in range(len(self.coefficients)):
            ans = ans.sum((other.power(len(self.coefficients) - i - 1)).scale(self.coefficients[i]))
        return ans


def do_some_operation(self, other, operations):
    assert isinstance(self, Polynomial) and isinstance(other, Polynomial)
    operations = "".join(operations.split())
    if operations[0] + operations[1] == "P1":
        operations = operations[2::]
        if len(operations) == 0:
            return Polynomial(self.coefficients)
        elif operations[0] == "+":
            operations = operations[1::]
            return self.sum(do_some_operation(self, other, operations))
        elif operations[0] == "-":
            operations = operations[1::]
            return self.difference(do_some_operation(self, other, operations))
        elif operations[0] == "*":
            operations = operations[1::]
            return self.product(do_some_operation(self, other, operations))
    elif operations[0] + operations[1] == "P2":
        operations = operations[2::]
        if len(operations) == 0:
            return Polynomial(other.coefficients)
        elif operations[0] == "+":
            operations = operations[1::]
            return other.sum(do_some_operation(self, other, operations))
        elif operations[0] == "-":
            operations = operations[1::]
            return other.difference(do_some_operation(self, other, operations))
        elif operations[0] == "*":
            operations = operations[1::]
            return other.product(do_some_operation(self, other, operations))
    else:
        print("I am stupid calculator, I can not count your input")


coef = input()
p = Polynomial(coef)
p.get_view()

coef = input()
q = Polynomial(coef)
q.get_view()

p.product(q).get_view()
p.sum(q).get_view()

# print(Polynomial.get_count())
string = input()
# p.do_some_operation(q, string).get_view()
do_some_operation(p, q, string).get_view()
