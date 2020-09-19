from old_grand_system import *


# new grand system


class ModernStipendManager(StipendManager):

    def who_gets_money(self):
        # work part
        list_of_good_students = []  # 45% of students with good marks
        list_of_excellent_students = []  # 10% of good students
        list_of_exemption_students = []

        candidates = []
        for student in self.students:
            if student.has_only_good_marks():
                candidates.append([student, student.average_mark()])
        candidates.sort(key=lambda i: i[1], reverse=True)

        num_of_granted_students = min(int(0.45 * len(self.students)), len(candidates))
        num_of_excellent_students = int(num_of_granted_students * 0.1)
        for i in range(len(candidates)):
            if i < num_of_excellent_students:
                candidates[i][0].grant = ModernStipendManager.big_grant
                list_of_excellent_students.append(candidates[i][0])
            elif i < num_of_granted_students:
                candidates[i][0].grant = ModernStipendManager.normal_grant
                list_of_good_students.append(candidates[i][0])
            elif candidates[i][0].can_get_social:
                candidates[i][0].grant = ModernStipendManager.social_grant
                list_of_exemption_students.append(candidates[i][0])

        return list_of_good_students, list_of_excellent_students, list_of_exemption_students

    def print_results_to_the_file(self, path):
        # print part
        list_of_good_students, list_of_excellent_students, list_of_exemption_students = self.who_gets_money()
        file = open(path, "w", encoding="utf-8")
        counter = 0
        file.write("          Підвищена стипендія: \n")
        for student in list_of_excellent_students:
            counter += 1
            file.write(str(counter) + ") " + student.name + " " + student.surname + ", номер квитка: " +
                       student.id_number + ", бал: " + str(student.average_mark()) + ", " +
                       str(student.grant) + "грн" + "\n")

        file.write("\n")
        file.write("          Звичайна стипендія: \n")
        for student in list_of_good_students:
            counter += 1
            file.write(str(counter) + ") " + student.name + " " + student.surname + ", номер квитка: " +
                       student.id_number + ", бал: " + str(student.average_mark()) + ", " +
                       str(student.grant) + "грн" + "\n")

        file.write("\n")
        file.write("          Соціальна стипендія: \n")
        for student in list_of_exemption_students:
            counter += 1
            file.write(str(counter) + ") " + student.name + " " + student.surname + ", номер квитка: " +
                       student.id_number + ", " + str(student.grant) + "грн" + "\n")

        file.close()


if __name__ == "__main__":
    a = ModernStipendManager("Students.txt")
    a.print_results_to_the_file("Students with grants (new system).txt")

    print(a.average_mark())
    print(a.average_mark("Соціальна стипендія"))
