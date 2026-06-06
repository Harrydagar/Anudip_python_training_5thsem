"""
6. Student Attendance Tracker
Problem Statement
Attendance for 15 days is recorded as:
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']
Write a program to:
•
Count present and absent days.
•
Calculate attendance percentage.
•
Determine eligibility (minimum 75% attendance).
•
Display positions where the student was absent.
"""

# Attendance record
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

present = 0
absent = 0

print("Absent Positions:")

for i in range(len(attendance)):

    if attendance[i] == 'P':
        present += 1
    else:
        absent += 1
        print(i + 1)

percentage = (present * 100) / len(attendance)

print("\nPresent Days:", present)
print("Absent Days:", absent)
print("Attendance Percentage:", percentage)

if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")