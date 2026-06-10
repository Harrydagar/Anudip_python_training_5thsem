def load_employees():
    employees = []

    file = open("employees.txt", "r")

    for line in file:
        emp_id, name, salary = line.strip().split(",")
        employees.append(
            {
                "id": emp_id,
                "name": name,
                "salary": int(salary)
            }
        )

    file.close()
    return employees


def save_employees(employees):
    file = open("employees.txt", "w")

    for emp in employees:
        file.write(f"{emp['id']},{emp['name']},{emp['salary']}\n")

    file.close()


def display_records(employees):
    print("\nEmployee Records")
    for emp in employees:
        print(emp["id"], emp["name"], emp["salary"])


def search_employee(employees):
    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:
            print(emp)
            return

    print("Employee not found")


def average_salary(employees):
    total = 0

    for emp in employees:
        total += emp["salary"]

    print("Average Salary =", total / len(employees))


def highest_lowest(employees):
    highest = employees[0]
    lowest = employees[0]

    for emp in employees:
        if emp["salary"] > highest["salary"]:
            highest = emp

        if emp["salary"] < lowest["salary"]:
            lowest = emp

    print("Highest Paid Employee:")
    print(highest)

    print("Lowest Paid Employee:")
    print(lowest)


def above_50000(employees):
    print("\nEmployees earning above 50000")

    for emp in employees:
        if emp["salary"] > 50000:
            print(emp)


def add_employee(employees):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    salary = int(input("Enter Salary: "))

    employees.append(
        {
            "id": emp_id,
            "name": name,
            "salary": salary
        }
    )

    save_employees(employees)

    print("Employee Added Successfully")


def salary_categories(employees):
    print("\nSalary Categories")

    for emp in employees:

        if emp["salary"] >= 60000:
            category = "High"

        elif emp["salary"] >= 40000:
            category = "Medium"

        else:
            category = "Low"

        print(emp["name"], "->", category)


def main():

    employees = load_employees()

    while True:

        print("\n===== Employee Payroll Management =====")
        print("1. Display All Employees")
        print("2. Search Employee")
        print("3. Average Salary")
        print("4. Highest and Lowest Paid")
        print("5. Employees Above 50000")
        print("6. Add Employee")
        print("7. Salary Categories")
        print("8. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            display_records(employees)

        elif choice == 2:
            search_employee(employees)

        elif choice == 3:
            average_salary(employees)

        elif choice == 4:
            highest_lowest(employees)

        elif choice == 5:
            above_50000(employees)

        elif choice == 6:
            add_employee(employees)
            employees = load_employees()

        elif choice == 7:
            salary_categories(employees)

        elif choice == 8:
            print("Program Ended")
            break

        else:
            print("Invalid Choice")


main()