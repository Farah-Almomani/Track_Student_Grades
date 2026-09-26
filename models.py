import matplotlib.pyplot as plt

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, score):
        if  score >= 0 and score <= 100:
            self.grades[subject] = score
            return True
        return False
    def get_average(self):
        if not self.grades:
            return 0
        else:
            return sum(self.grades.values()) / len(self.grades)
    def get_letter_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    def display(self):
        print("Student name: {}".format(self.name))
        for subject, score in self.grades.items():
            print("\t{}: {}".format(subject, score))
        print("Avg: {}".format(self.get_average()))
        print("Letter Grade: {}".format(self.get_letter_grade()))

class HonorStudent(Student):
    def __init__(self, name):
        super().__init__(name)
    def is_scholarship(self):
        return self.get_average() >= 90
    def display(self):
        super().display()
        if self.is_scholarship():
            print("Scholarship: Yes")
        else:
            print("Scholarship: No")

class GradeBook:
    def __init__(self):
        self.students = []
    def add_student(self, name):
        for student in self.students:
            if student.name == name:
                print("Student {} already exists!".format(name))
                return
        self.students.append(Student(name))
        print("Student {} added!".format(name))
    def find_student(self, name):
        for student in self.students:
            if name.lower() in student.name.lower():
                return student
        return None
    def class_report(self):
        if len(self.students) == 0:
            print("No students found!")
            return
        sorted_students = sorted(self.students, key=lambda student: student.get_average(), reverse=True)
        i = 1
        for student in sorted_students:
            print(i, "- ", student.name, "Average:", student.get_average())
            i += 1

    def class_statistics(self):
        if not self.students:
            print("No students found!")
            return
        averages = [student.get_average() for student in self.students]
        print("Number of students: ",len(self.students))
        print("Class average: ",sum(averages) / len(averages))
        print("Highest average: ", max(averages))
        print("Lowest average: ", min(averages))
        FailedStudents = []
        PassStudents = []
        for student in self.students:
            if student.get_letter_grade() == 'F':
                FailedStudents.append(student)
            else:
                PassStudents.append(student)
        print("Number of Failed Students: ",len(FailedStudents))
        print("Number of Passed Students: ",len(PassStudents))
    def top_students(self, n =3):
        if not self.students:
            print("No students found!")
            return

        sorted_students = sorted(self.students, key=lambda student: student.get_average(), reverse=True)
        top = sorted_students[:n]
        print("Top {} students:".format(n))
        i = 1
        for student in top:
            print(i, "- ",student.name, " - ", student.get_average(), " - ", student.get_letter_grade())

    def show_charts(self):
        if not self.students:
            print("No students found!")
            return
        subjects = set()
        for student in self.students:
            for subject in student.grades.keys():
                subjects.add(subject)

        subject_names = []
        subject_averages = []
        for subject in subjects:
            total = 0
            count = 0
            for student in self.students:
                if subject in student.grades:
                    total += student.grades[subject]
                    count += 1
            if count > 0:
                subject_names.append(subject)
                subject_averages.append(total / count)
        plt.bar(subject_names, subject_averages)
        plt.title("Subject Averages")
        plt.xlabel("Subject")
        plt.ylabel("Average")
        plt.show()

        Marks = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for student in self.students:
            Marks[student.get_letter_grade()] += 1
        labels = []
        sizes = []
        for grade, count in Marks.items():
            if count > 0:
                labels.append(grade)
                sizes.append(count)

        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title("Grades")
        plt.show()
    def add_honor_student(self, name):
        for student in self.students:
            if student.name == name:
                print("Student {} already exists!".format(name))
                return
        self.students.append(HonorStudent(name))
        print("Honor Student {} added!".format(name))

