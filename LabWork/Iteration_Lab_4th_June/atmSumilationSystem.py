# ATM Simulation System

# Initial balance
balance = 10000

# Infinite loop to keep showing the menu
while True:

    # Display ATM Menu
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    # Take user choice
    choice = int(input("Enter your choice: "))

    # Option 1:Check Balance
    if choice == 1:
        print("Current Balance: ₹", balance)

    # Option 2:Deposit Money
    elif choice == 2:
        deposit = float(input("Enter amount to deposit: ₹"))

        # Validation
        if deposit <= 0:
            print("Deposit amount must be greater than 0.")
        else:
            balance += deposit
            print("₹", deposit, "deposited successfully.")
            print("Updated Balance: ₹", balance)

    # Option 3: Withdraw Money
    elif choice == 3:
        withdraw = float(input("Enter amount to withdraw: ₹"))

        # Validation
        if withdraw <= 0:
            print("Withdrawal amount must be greater than 0.")

        # Check if sufficient balance exists
        elif withdraw > balance:
            print("Insufficient Balance!")

        else:
            balance -= withdraw
            print("₹", withdraw, "withdrawn successfully.")
            print("Remaining Balance: ₹", balance)

    # Option 4: Exit ATM
    elif choice == 4:
        print("Thank you for using our ATM!")
        break

    # Invalid Choice
    else:
        print("Invalid choice! Please select between 1 and 4.")