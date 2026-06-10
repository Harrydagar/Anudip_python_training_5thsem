"""1. Student Performance Analytics System
Problem Statement
A coaching institute wants to analyze student performance.
Store details of at least 30 students in a dictionary.
Example Structure
students = { "S101": {"name": "Anuj", "marks": 85}, "S102": {"name": "Rahul", "marks": 72} }
Requirements
1.
Display all student records.
2.
Search a student using Student ID.
3.
Add a new student.
4.
Update marks of an existing student.
5.
Delete a student.
6.
Find topper and lowest scorer.
7.
Calculate class average.
8.
Count pass and fail students.
9.
Generate grades:
o
A (90+)
o
B (75–89)
o
C (50–74)
o
F (<50)
10.
Display students scoring above average.
11.
Display top 5 performers.
12.
Create a separate dictionary for scholarship students (marks > 85).
Expected Learning
•
Nested Dictionaries
•
Dictionary Traversal
•
Searching
•
Aggregation
•
Report Generation"""


# ==============================
# Student Performance Analytics System
# ==============================

students = {
"S101":{"name":"Aman","marks":91},
"S102":{"name":"Rohan","marks":72},
"S103":{"name":"Priya","marks":88},
"S104":{"name":"Karan","marks":65},
"S105":{"name":"Anjali","marks":95},
"S106":{"name":"Vikas","marks":48},
"S107":{"name":"Neha","marks":79},
"S108":{"name":"Mohit","marks":84},
"S109":{"name":"Riya","marks":56},
"S110":{"name":"Pooja","marks":90},
"S111":{"name":"Rahul","marks":67},
"S112":{"name":"Nitin","marks":73},
"S113":{"name":"Simran","marks":98},
"S114":{"name":"Aakash","marks":44},
"S115":{"name":"Deepak","marks":81},
"S116":{"name":"Kriti","marks":77},
"S117":{"name":"Meena","marks":69},
"S118":{"name":"Aryan","marks":92},
"S119":{"name":"Tina","marks":53},
"S120":{"name":"Yash","marks":87},
"S121":{"name":"Ritu","marks":61},
"S122":{"name":"Arjun","marks":75},
"S123":{"name":"Sahil","marks":49},
"S124":{"name":"Komal","marks":82},
"S125":{"name":"Nisha","marks":94},
"S126":{"name":"Harsh","marks":89},
"S127":{"name":"Ravi","marks":71},
"S128":{"name":"Sneha","marks":58},
"S129":{"name":"Manish","marks":96},
"S130":{"name":"Payal","marks":66}
}

# ==============================
# Functions
# ==============================

def display_students():
    print("\nSTUDENT RECORDS")
    print("-" * 40)

    for sid in students:
        print(
            sid,
            students[sid]["name"],
            students[sid]["marks"]
        )


def search_student():
    sid = input("Enter Student ID: ")

    if sid in students:
        print("\nRecord Found")
        print("Name :", students[sid]["name"])
        print("Marks:", students[sid]["marks"])
    else:
        print("Student Not Found")


def add_student():
    sid = input("Enter Student ID: ")

    if sid in students:
        print("Student ID already exists")
    else:
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        students[sid] = {
            "name": name,
            "marks": marks
        }

        print("Student Added Successfully")


def update_marks():
    sid = input("Enter Student ID: ")

    if sid in students:
        new_marks = float(input("Enter New Marks: "))
        students[sid]["marks"] = new_marks
        print("Marks Updated")
    else:
        print("Student Not Found")


def delete_student():
    sid = input("Enter Student ID: ")

    if sid in students:
        del students[sid]
        print("Student Deleted")
    else:
        print("Student Not Found")


def topper():
    highest = -1
    topper_id = ""

    for sid in students:
        if students[sid]["marks"] > highest:
            highest = students[sid]["marks"]
            topper_id = sid

    print("\nTOPPER")
    print(topper_id,
          students[topper_id]["name"],
          highest)


def lowest_scorer():
    lowest = 101
    lowest_id = ""

    for sid in students:
        if students[sid]["marks"] < lowest:
            lowest = students[sid]["marks"]
            lowest_id = sid

    print("\nLOWEST SCORER")
    print(lowest_id,
          students[lowest_id]["name"],
          lowest)


def class_average():
    total = 0

    for sid in students:
        total += students[sid]["marks"]

    avg = total / len(students)

    print("\nClass Average =", round(avg, 2))
    return avg


def pass_fail_count():

    passed = 0
    failed = 0

    for sid in students:

        if students[sid]["marks"] >= 50:
            passed += 1
        else:
            failed += 1

    print("\nPass Students :", passed)
    print("Fail Students :", failed)


def generate_grades():

    print("\nGRADE REPORT")
    print("-" * 50)

    for sid in students:

        marks = students[sid]["marks"]

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        else:
            grade = "F"

        print(
            sid,
            students[sid]["name"],
            marks,
            grade
        )


def above_average_students():

    total = 0

    for sid in students:
        total += students[sid]["marks"]

    avg = total / len(students)

    print("\nStudents Above Average")
    print("Average =", round(avg, 2))

    for sid in students:
        if students[sid]["marks"] > avg:
            print(
                sid,
                students[sid]["name"],
                students[sid]["marks"]
            )


def top_five_students():

    print("\nTOP 5 PERFORMERS")
    print("-" * 40)

    temp = students.copy()

    count = 0

    while count < 5 and len(temp) > 0:

        best_id = ""
        best_marks = -1

        for sid in temp:

            if temp[sid]["marks"] > best_marks:
                best_marks = temp[sid]["marks"]
                best_id = sid

        print(
            count + 1,
            temp[best_id]["name"],
            temp[best_id]["marks"]
        )

        del temp[best_id]

        count += 1


def scholarship_students():

    scholarship = {}

    for sid in students:

        if students[sid]["marks"] > 85:
            scholarship[sid] = students[sid]

    print("\nSCHOLARSHIP STUDENTS")
    print("-" * 40)

    for sid in scholarship:
        print(
            sid,
            scholarship[sid]["name"],
            scholarship[sid]["marks"]
        )


# ==============================
# Main Menu
# ==============================

while True:

    print("\n")
    print("=" * 50)
    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 50)

    print("1. Display All Students")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. Find Lowest Scorer")
    print("8. Calculate Average")
    print("9. Pass/Fail Count")
    print("10. Generate Grades")
    print("11. Students Above Average")
    print("12. Top 5 Performers")
    print("13. Scholarship Students")
    print("0. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        display_students()

    elif choice == "2":
        search_student()

    elif choice == "3":
        add_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        topper()

    elif choice == "7":
        lowest_scorer()

    elif choice == "8":
        class_average()

    elif choice == "9":
        pass_fail_count()

    elif choice == "10":
        generate_grades()

    elif choice == "11":
        above_average_students()

    elif choice == "12":
        top_five_students()

    elif choice == "13":
        scholarship_students()

    elif choice == "0":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")