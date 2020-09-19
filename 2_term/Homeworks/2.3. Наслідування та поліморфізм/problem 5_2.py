# 76, 70, 68, 67, 68, after exercises 74, 76


class Matrix:
    def __init__(self, lines):
        if isinstance(lines, str):
            f = open(lines)
            lst = []
            for line in f:
                ol = line.split()
                nl = [float(i) for i in ol]
                lst.append(nl)
            f.close()

            p = True
            for i in range(len(lst) - 1):
                if len(lst[i]) != len(lst[i + 1]):
                    p = False
                    break
            if len(lst) != len(lst[0]):
                p = False
            assert p

            self.lines = lst

        elif isinstance(lines, Matrix):
            self.lines = lines.lines
        else:
            p = True
            for i in range(len(lines) - 1):
                if len(lines[i]) != len(lines[i + 1]):
                    p = False
                    break
            if len(lines) != len(lines[0]):
                p = False
            assert p
            self.lines = lines

    def show(self, file=""):
        if file == "":
            for i in range(len(self.lines)):
                # print(" ", end="")
                for j in range(len(self.lines[i])):
                    print(self.lines[i][j], end="")
                    print(" ", end="")
                print(" ")
        else:
            f = open(file, "w")
            for i in range(len(self.lines)):
                for j in range(len(self.lines[i])):
                    f.write(str(self.lines[i][j]))
                    f.write(" ")
                f.write("\n")
            f.close()

    def determinant(self):
        pass

    def is_degenerate(self):
        return self.determinant() == 0


class Matrix2D(Matrix):
    def __init__(self, lines):
        super().__init__(lines)
        assert len(self.lines) == 2

    def determinant(self):
        return self.lines[0][0] * self.lines[1][1] - self.lines[1][0] * self.lines[0][1]


class Matrix3D(Matrix):
    def __init__(self, lines):
        super().__init__(lines)
        assert len(self.lines) == 3

    def determinant(self):
        m = [0, 0, 0]
        m[0] = Matrix2D([[self.lines[1][1], self.lines[1][2]],
                         [self.lines[2][1], self.lines[2][2]]])
        m[1] = Matrix2D([[self.lines[1][0], self.lines[1][2]],
                         [self.lines[2][0], self.lines[2][2]]])
        m[2] = Matrix2D([[self.lines[1][0], self.lines[1][1]],
                         [self.lines[2][0], self.lines[2][1]]])
        res = 0
        for i in range(3):
            res += (-1) ** i * self.lines[0][i] * m[i].determinant()
        return res


class Vector:
    def __init__(self, column):
        if isinstance(column, str):
            f = open(column)
            lines = f.readlines()
            line = lines[-1]
            ol = line.split()
            nl = [float(i) for i in ol]
            f.close()

            self.column = nl

        elif isinstance(column, Vector):
            self.column = column.column

        else:
            self.column = column

    def show(self, file=""):
        if file == "":
            for i in range(len(self.column)):
                print(self.column[i], end="")
                print(" ", end="")
            print(" ")
        else:
            f = open(file, "w")
            for i in range(len(self.column)):
                f.write(str(self.column[i]))
                f.write(" ")
            f.write("\n")
            f.close()


class Vector2D(Vector):
    def __init__(self, column):
        super().__init__(column)
        assert len(self.column) == 2


class Vector3D(Vector):
    def __init__(self, column):
        super().__init__(column)
        assert len(self.column) == 3


class Solver:
    def __init__(self, matrix, vector):
        assert isinstance(matrix, Matrix3D) and isinstance(vector, Vector3D)
        self.matrix = matrix
        self.vector = vector

    def get_solution(self):
        if self.matrix.is_degenerate():
            return "matrix is degenerate"
        else:
            delta = self.matrix.determinant()
            matrix1 = Matrix3D([[self.vector.column[0], self.matrix.lines[0][1], self.matrix.lines[0][2]],
                                [self.vector.column[1], self.matrix.lines[1][1], self.matrix.lines[1][2]],
                                [self.vector.column[2], self.matrix.lines[2][1], self.matrix.lines[2][2]]])
            delta1 = matrix1.determinant()
            matrix2 = Matrix3D([[self.matrix.lines[0][0], self.vector.column[0], self.matrix.lines[0][2]],
                                [self.matrix.lines[1][0], self.vector.column[1], self.matrix.lines[1][2]],
                                [self.matrix.lines[2][0], self.vector.column[2], self.matrix.lines[2][2]]])
            delta2 = matrix2.determinant()
            matrix3 = Matrix3D([[self.matrix.lines[0][0], self.matrix.lines[0][1], self.vector.column[0]],
                                [self.matrix.lines[1][0], self.matrix.lines[1][1], self.vector.column[1]],
                                [self.matrix.lines[2][0], self.matrix.lines[2][1], self.vector.column[2]]])
            delta3 = matrix3.determinant()
            return Vector3D([delta1 / delta, delta2 / delta, delta3 / delta])


M = Matrix3D("text.txt")
print("matrix of coefficients:")
M.show()
print()
V = Vector3D("new_text.txt")
print("free column:  ", end="")
V.show()
print()

S = Solver(M, V)
print("solution:  ", end="")
S.get_solution().show()
