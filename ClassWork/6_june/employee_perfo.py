"""
Question 1: Employee Performance Evaluation
Problem Statement
A company stores employee details in a tuple. Each employee record contains:
employees = ( ("E101", "Anuj", 92), ("E102", "Rahul", 76), ("E103", "Priya", 58), ("E104", "Neha", 88), ("E105", "Amit", 45) )

Where:
• First value = Employee ID
• Second value = Employee Name
• Third value = Performance Score

Tasks
Write a Python program to:
1. Display details of employees scoring 80 or above.
2. Count the number of employees who need improvement (score below 60).
3. Find the employee with the highest score.
4. Create a list containing the names of all employees scoring above 75.
5. Display the performance category for each employee:

90 and above → Excellent
75 to 89 → Good
60 to 74 → Average
Below 60 → Needs Improvement"""
#----------------------------------------------------------------------------------------------------------------------

# Employee records stored in tuple
employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)

print("Employees Scoring 80 or Above:")

# Initialize variables
improvement = 0
high_performers = []

# Assume first employee has highest score
highest = employees[0]

# Process employee records
for emp in employees:

    # Display employees scoring 80 or above
    if emp[2] >= 80:
        print(emp[0], emp[1], emp[2])

    # Count employees needing improvement
    if emp[2] < 60:
        improvement += 1

    # Find highest performer
    if emp[2] > highest[2]:
        highest = emp

    # Create list of employees scoring above 75
    if emp[2] > 75:
        high_performers.append(emp[1])

print("Employees Needing Improvement:", improvement)

print("Highest Performer:")
print(highest[0], highest[1], highest[2])

print("High Performers:")
print(high_performers)

print("Performance Categories:")

# Display performance category
for emp in employees:

    if emp[2] >= 90:
        category = "Excellent"
    elif emp[2] >= 75:
        category = "Good"
    elif emp[2] >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"

    print(emp[1], "->", category)