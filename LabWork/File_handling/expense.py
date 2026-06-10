def load_expenses():

    expenses = {}

    file = open("expenses.txt", "r")

    for line in file:

        category, amount = line.strip().split(",")

        expenses[category] = int(amount)

    file.close()

    return expenses


def save_expenses(expenses):

    file = open("expenses.txt", "w")

    for category, amount in expenses.items():

        file.write(f"{category},{amount}\n")

    file.close()


def display_expenses(expenses):

    print("\nExpense Records")

    for category, amount in expenses.items():

        print(category, "-", amount)


def total_expenses(expenses):

    total = 0

    for amount in expenses.values():

        total += amount

    print("Total Expenditure = ₹", total)


def highest_lowest_expense(expenses):

    highest_category = max(expenses, key=expenses.get)
    lowest_category = min(expenses, key=expenses.get)

    print("\nHighest Expense")
    print(highest_category, "-", expenses[highest_category])

    print("\nLowest Expense")
    print(lowest_category, "-", expenses[lowest_category])


def expenses_above_800(expenses):

    print("\nExpenses Greater Than ₹800")

    found = False

    for category, amount in expenses.items():

        if amount > 800:

            print(category, "-", amount)

            found = True

    if not found:

        print("No Expense Above ₹800")


def add_expense(expenses):

    category = input("Enter New Category: ")
    amount = int(input("Enter Amount: "))

    expenses[category] = amount

    save_expenses(expenses)

    print("Expense Added Successfully")


def update_expense(expenses):

    category = input("Enter Category To Update: ")

    if category in expenses:

        amount = int(input("Enter New Amount: "))

        expenses[category] = amount

        save_expenses(expenses)

        print("Expense Updated Successfully")

    else:

        print("Category Not Found")


def generate_report(expenses):

    total = sum(expenses.values())

    highest_category = max(expenses, key=expenses.get)
    lowest_category = min(expenses, key=expenses.get)

    file = open("report.txt", "w")

    file.write("DAILY EXPENSE REPORT\n")
    file.write("====================\n\n")

    file.write(f"Total Expenses : ₹{total}\n\n")

    file.write(
        f"Highest Expense Category : {highest_category} "
        f"(₹{expenses[highest_category]})\n"
    )

    file.write(
        f"Lowest Expense Category : {lowest_category} "
        f"(₹{expenses[lowest_category]})\n\n"
    )

    file.write("Categories Spending More Than ₹800\n")

    for category, amount in expenses.items():

        if amount > 800:

            file.write(f"{category} - ₹{amount}\n")

    file.close()

    print("Report Generated Successfully in report.txt")


def main():

    expenses = load_expenses()

    while True:

        print("\n===== Daily Expense Tracker =====")
        print("1. Display All Expenses")
        print("2. Calculate Total Expenditure")
        print("3. Highest and Lowest Spending")
        print("4. Display Expenses Greater Than ₹800")
        print("5. Add New Expense Category")
        print("6. Update Existing Expense")
        print("7. Generate Summary Report")
        print("8. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            display_expenses(expenses)

        elif choice == 2:

            total_expenses(expenses)

        elif choice == 3:

            highest_lowest_expense(expenses)

        elif choice == 4:

            expenses_above_800(expenses)

        elif choice == 5:

            add_expense(expenses)

            expenses = load_expenses()

        elif choice == 6:

            update_expense(expenses)

            expenses = load_expenses()

        elif choice == 7:

            generate_report(expenses)

        elif choice == 8:

            print("Program Ended")
            break

        else:

            print("Invalid Choice")


main()