



# Student Result Management System

student_marks = {
    "Anuj": 85,
    "Rahul": 72,
    "Priya": 91,
    "Neha": 68,
    "Amit": 78
}

# 1. Display marks of Priya
print("Priya marks:", student_marks["Priya"])

# 2. Display marks of Amit
print("Amit marks:", student_marks["Amit"])

# 3. Update Rahul's marks from 72 to 80
student_marks["Rahul"] = 80
print("Rahul updated marks:", student_marks["Rahul"])

# 4. Check whether Rohan exists
found = False
for name in student_marks:
    if name == "Rohan":
        found = True
        break

if found:
    print("Rohan exists")
else:
    print("Rohan does not exist")

# 5. Display all student names
print("\nStudent Names:")
for name in student_marks:
    print(name)

# 6. Display all marks
print("\nStudent Marks:")
for name in student_marks:
    print(student_marks[name])

# 7. Find highest scorer
max_marks = student_marks["Anuj"]
topper = "Anuj"

for name in student_marks:
    if student_marks[name] > max_marks:
        max_marks = student_marks[name]
        topper = name

print("\nHighest scorer:", topper, "with marks", max_marks)

# 8. Add new student (Rohan : 88)
student_marks["Rohan"] = 88
print("\nRohan added")

# 9. Remove student (Neha)
if "Neha" in student_marks:
    del student_marks["Neha"]
    print("Neha removed")

# 10. Display all student records
print("\nFinal Student Records:")
for name in student_marks:
    print(name, ":", student_marks[name])