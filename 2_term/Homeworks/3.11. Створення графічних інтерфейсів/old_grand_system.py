from person_and_students import *


# old grand system


class StipendManager:
    # constants
    normal_grant = 1800
    big_grant = int(normal_grant * 1.2)
    social_grant = 1000

    def __init__(self, path):
        file = open(path, "r", encoding="utf-8")
        students_info_list = file.readlines()
        file.close()

        students = []
        for line in students_info_list:
            line = line[:-1:]
            demo_info = line.split(",")
            info = demo_info[0].split() + demo_info[1].split() + demo_info[2].split() + demo_info[3].split()
            marks = [int(b) for b in demo_info[4].split()]
            info.append(marks)
            info += demo_info[-1].split()

            students.append(Student(info))
        file.close()

        self.students = students

    def who_gets_money(self):
        # work part
        list_of_good_students = []
        list_of_excellent_students = []
        list_of_exemption_students = []
        for student in self.students:
            if student.has_only_excellent_marks():
                student.grant = StipendManager.big_grant
                list_of_excellent_students.append(student)
            elif student.has_only_good_marks() and student.average_mark() >= 75:
                student.grant = StipendManager.normal_grant
                list_of_good_students.append(student)
            elif student.can_get_social and student.has_only_good_marks():
                student.grant = StipendManager.social_grant
                list_of_exemption_students.append(student)

        return list_of_good_students, list_of_excellent_students, list_of_exemption_students

    def print_results_to_the_file(self, path):
        # print part
        list_of_good_students, list_of_excellent_students, list_of_exemption_students = self.who_gets_money()
        file = open(path, "w", encoding="utf-8")
        file.write("          Підвищена стипендія: \n")
        for student in list_of_excellent_students:
            file.write(student.name + " " + student.surname + ", номер квитка: " + student.id_number + ", " +
                       str(student.grant) + "грн" + "\n")

        file.write("\n")
        file.write("          Звичайна стипендія: \n")
        for student in list_of_good_students:
            file.write(student.name + " " + student.surname + ", номер квитка: " + student.id_number + ", " +
                       str(student.grant) + "грн" + "\n")

        file.write("\n")
        file.write("          Соціальна стипендія: \n")
        for student in list_of_exemption_students:
            file.write(student.name + " " + student.surname + ", номер квитка: " + student.id_number + ", " +
                       str(student.grant) + "грн" + "\n")

        file.close()

    def number_of_granted_students(self, category):
        if category == "Академічна стипендія":
            return len(self.who_gets_money()[0] + self.who_gets_money()[1])

        elif category == "Соціальна стипендія":
            return len(self.who_gets_money()[2])

        elif category == "Всі студенти":
            return len(self.students)

        elif category == "Стипендіанти":
            return len(self.who_gets_money()[0] + self.who_gets_money()[1] + self.who_gets_money()[2])

    def sum_of_grants(self, category="Всі студенти"):
        lst = None
        if category == "Академічна стипендія":
            lst = self.who_gets_money()[0] + self.who_gets_money()[1]

        elif category == "Соціальна стипендія":
            lst = self.who_gets_money()[2]

        elif category == "Всі студенти" or category == "Стипендіанти":
            lst = self.students

        ans = 0
        for student in lst:
            ans += student.grant
        return ans

    def average_mark(self, category="Академічна стипендія"):
        lst = []
        if category == "Академічна стипендія":
            lst = self.who_gets_money()[0] + self.who_gets_money()[1]
        elif category == "Соціальна стипендія":
            lst = self.who_gets_money()[2]
        elif category == "Всі студенти":
            lst = self.students
        elif category == "Стипендіанти":
            lst = self.who_gets_money()[0] + self.who_gets_money()[1] + self.who_gets_money()[2]
        ans = 0
        for student in lst:
            ans += student.average_mark()
        if len(lst) != 0:
            ans = ans / len(lst)
        return ans


if __name__ == "__main__":
    a = StipendManager("Students.txt")
    a.print_results_to_the_file("Students with grants (old system).txt")

    print(a.average_mark())
    print(a.average_mark("Соціальна стипендія"))
