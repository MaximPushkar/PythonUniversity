class Person:

    def __init__(self, info):
        self.name = info[0]
        self.surname = info[1]
        self.gender = info[2]

    def __str__(self):
        return self.name + " " + self.surname + ", " + self.gender


class Student(Person):

    def __init__(self, info):
        super().__init__(info)
        self.id_number = info[4]
        self.specialty = info[3]
        self.exam_results = info[5]
        self.can_get_social = False
        if info[6] == "звичайний":
            self.can_get_social = False
        elif info[6] == "пільговик":
            self.can_get_social = True
        self.grant = 0

    def __str__(self):
        return self.name + " " + self.surname + " " + self.gender + " " + self.specialty + " " + self.id_number \
               + " " + str(self.exam_results) + " " + str(self.can_get_social)

    def has_only_good_marks(self):
        for mark in self.exam_results:
            if mark < 60:
                return False
        return True

    def has_only_excellent_marks(self):
        for mark in self.exam_results:
            if mark < 90:
                return False
        return True

    def average_mark(self):
        ans = 0
        for mark in self.exam_results:
            ans += mark
        ans = ans / len(self.exam_results)
        return ans
