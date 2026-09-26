import models as m

def show():
    print("*" * 35)
    print("Grades Tracker")
    print("*"*35)

    print("1. Add Student       2. Add Grades")
    print("3. View Student      4. Class Report")
    print("5. Top Student       6. Statistics")
    print("7. Filter By Grade   8. Compare 2 students")
    print("9. Exit")

def main():
    grade_book = m.GradeBook()
    while True:
        show()
        try:
            choice = int(input("Enter Choice: "))
            if choice < 1 or choice > 9:
                print("choice must be between 1 and 9")
                continue
        except ValueError:
            print("Please enter a number")
            continue

        if choice == 1:
            student_name = input("Enter Student Name: ")
            if not student_name:
                print("Name cannot be empty")
            elif student_name.isdigit():
                print("Name cannot be a number")
            else:
                is_honor = input("Is Honor? (y/n): ").lower()
                if is_honor == "y":
                    grade_book.add_honor_student(student_name)
                else:
                    grade_book.add_student(student_name)

        elif choice == 2:
            student_name = input("Enter Student Name: ")
            student = grade_book.find_student(student_name)
            if student:
                while True:
                    subject = input("Enter Subject or 'done' to finish: ")
                    if subject.lower() == "done":
                        break
                    str_score = input("Enter Score: ")
                    try:
                        score = float(str_score)
                        if score >= 0 and score <= 100:
                            student.add_grade(subject, score)
                            print("Grade added Successfully")
                        else:
                            print("Score must be between 0 and 100")
                    except ValueError:
                        print("Invalid Score")

            else:
                print("Student {} does not exist!".format(student_name))

        elif choice == 3:
            student_name = input("Enter Student Name: ")
            student = grade_book.find_student(student_name)
            if student:
                student.display()
            else:
                print("Student {} does not exist!".format(student_name))

        elif choice == 4:
            grade_book.class_report()

        elif choice == 5:
            grade_book.top_students()

        elif choice == 6:
            grade_book.class_statistics()
            grade_book.show_charts()

        elif choice == 7:
            a_students = list(filter(lambda student: student.get_letter_grade() == "A", grade_book.students))
            if a_students:
                print("Student with grade A:")
                i = 1
                for student in a_students:
                    print(i, "- ", student.name, " - Avg: ", student.get_average())
                    i = i + 1
            else:
                print("No Student with grade A")
        elif choice == 8:
            name1 = input("Enter First Student Name: ")
            name2 = input("Enter Second Student Name: ")
            student1 = grade_book.find_student(name1)
            student2 = grade_book.find_student(name2)
            if student1 and student2:
                subject = input("Enter Subject to compare: ")
                if subject in student1.grades and subject in student2.grades:
                    print("{}: {}".format(name1, student1.grades[subject]))
                    print("{}: {}".format(name2, student2.grades[subject]))
                    if student1.grades[subject] > student2.grades[subject]:
                        print("{} is higher than {}".format(name1, name2))
                    elif student1.grades[subject] < student2.grades[subject]:
                        print("{} is higher than {}".format(name2, name1))
                    else:
                        print("{} is the same score as {}".format(name1, name2))
                else:
                    print("{} or {} or both don't have this subject".format(name1, name2))
            else:
                if not student1:
                    print("Student {} does not exist!".format(name1))
                if not student2:
                    print("Student {} does not exist!".format(name2))
        elif choice == 9:
            print("Goodbye")
            break
        else:
            print("Invalid Choice")

        input("Press Enter to continue...")




if __name__ == '__main__':
    main()