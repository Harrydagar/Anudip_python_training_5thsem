"""
4. Employee Salary Processing
Problem Statement
Employee data is stored as tuples:
employees = [ ("Rahul", 35000), ("Priya", 55000), ("Amit", 42000), ("Neha", 65000) ]
Write a program to:
• Display employees earning above ₹50,000.
• Find the highest-paid employee.
• Calculate total salary expenditure.
• Count employees earning below ₹40,000."""

# Employee name and salary
employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# Assume first employee has highest salary
highest_paid = employees[0]

total_salary = 0
below_40000 = 0

print("Employees Earning Above ₹50,000:")

# Process employee records
for emp in employees:

    # Display salary above 50000
    if emp[1] > 50000:
        print(emp[0], "-", emp[1])

    # Find highest salary
    if emp[1] > highest_paid[1]:
        highest_paid = emp

    # Calculate total salary expenditure
    total_salary += emp[1]

    # Count employees below 40000
    if emp[1] < 40000:
        below_40000 += 1

print("\nHighest Paid Employee:")
print(highest_paid[0], "-", highest_paid[1])

print("Total Salary Expenditure:", total_salary)
print("Employees Earning Below ₹40,000:", below_40000)