def count_attendance():
    present = 0
    absent = 0

    file = open("attendance.txt", "r")

    for line in file:
        emp, status = line.strip().split(",")

        if status == "P":
            present += 1
        else:
            absent += 1

    file.close()

    print("Present Employees:", present)
    print("Absent Employees:", absent)

    return present, absent


def absent_employees():
    file = open("attendance.txt", "r")

    print("\nAbsent Employee IDs:")

    for line in file:
        emp, status = line.strip().split(",")

        if status == "A":
            print(emp)

    file.close()


def attendance_percentage():
    present, absent = count_attendance()

    percentage = (present / (present + absent)) * 100

    print("\nAttendance Percentage:", round(percentage, 1), "%")


def generate_absent_report():
    file = open("attendance.txt", "r")
    report = open("absent_report.txt", "w")

    for line in file:
        emp, status = line.strip().split(",")

        if status == "A":
            report.write(emp + "\n")

    file.close()
    report.close()

    print("\nAbsentee Report Generated Successfully.")


def attendance_award():
    print("\nAttendance Award Eligibility:")
    print("Not Applicable")


count_attendance()
absent_employees()
attendance_percentage()
generate_absent_report()
attendance_award()