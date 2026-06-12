def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def generate_report():
    file = open("marks.txt", "r")
    report = open("report_card.txt", "w")

    topper_name = ""
    topper_marks = 0

    passed = 0
    failed = 0

    merit_students = []

    for line in file:
        sid, name, marks = line.strip().split(",")
        marks = int(marks)

        grade = calculate_grade(marks)

        report.write(f"{sid},{name},{marks},{grade}\n")

        if marks > topper_marks:
            topper_marks = marks
            topper_name = name

        if marks >= 40:
            passed += 1
        else:
            failed += 1

        if marks >= 90:
            merit_students.append(name)

    file.close()
    report.close()

    print("\nTopper:")
    print(f"{topper_name} ({topper_marks})")

    print("\nPassed Students:", passed)
    print("Failed Students:", failed)

    print("\nMerit Certificate Students:")
    for student in merit_students:
        print(student)

    print("\nReport Card Generated Successfully.")


# Main Program
generate_report()