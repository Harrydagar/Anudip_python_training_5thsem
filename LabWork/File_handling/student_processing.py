def load_students():

    students = []

    file = open("results.txt", "r")

    for line in file:

        sid, name, marks = line.strip().split(",")

        students.append(
            {
                "id": sid,
                "name": name,
                "marks": int(marks)
            }
        )

    file.close()

    return students


def display_students(students):

    print("\nStudent Records")

    for student in students:

        print(student["id"],
              student["name"],
              student["marks"])


def search_student(students):

    sid = input("Enter Student ID: ")

    for student in students:

        if student["id"] == sid:

            print("\nStudent Found")
            print("ID    :", student["id"])
            print("Name  :", student["name"])
            print("Marks :", student["marks"])

            return

    print("Student Not Found")


def topper_lowest(students):

    topper = students[0]
    lowest = students[0]

    for student in students:

        if student["marks"] > topper["marks"]:
            topper = student

        if student["marks"] < lowest["marks"]:
            lowest = student

    print("\nTopper")
    print(topper)

    print("\nLowest Scorer")
    print(lowest)


def class_average(students):

    total = 0

    for student in students:

        total += student["marks"]

    avg = total / len(students)

    print("Class Average =", avg)


def pass_fail(students):

    passed = 0
    failed = 0

    for student in students:

        if student["marks"] >= 40:
            passed += 1

        else:
            failed += 1

    print("Passed Students :", passed)
    print("Failed Students :", failed)


def calculate_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 40:
        return "C"

    else:
        return "F"


def display_grades(students):

    print("\nGrade Report")

    for student in students:

        grade = calculate_grade(student["marks"])

        print(student["id"],
              student["name"],
              student["marks"],
              grade)


def write_grade_report(students):

    file = open("grades.txt", "w")

    file.write("Student Grade Report\n")
    file.write("----------------------\n")

    for student in students:

        grade = calculate_grade(student["marks"])

        file.write(
            f"{student['id']},{student['name']},{student['marks']},{grade}\n"
        )

    file.close()

    print("Grade Report Written To grades.txt")


def main():

    students = load_students()

    while True:

        print("\n===== Student Result Processing System =====")
        print("1. Display All Student Records")
        print("2. Search Student")
        print("3. Find Topper and Lowest Scorer")
        print("4. Calculate Class Average")
        print("5. Count Pass and Fail Students")
        print("6. Generate Grades")
        print("7. Write Grade Report")
        print("8. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            display_students(students)

        elif choice == 2:

            search_student(students)

        elif choice == 3:

            topper_lowest(students)

        elif choice == 4:

            class_average(students)

        elif choice == 5:

            pass_fail(students)

        elif choice == 6:

            display_grades(students)

        elif choice == 7:

            write_grade_report(students)

        elif choice == 8:

            print("Program Ended")
            break

        else:

            print("Invalid Choice")


main()