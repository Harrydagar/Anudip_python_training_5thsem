# Problem Statement: 
# Input transaction amounts continuously. 
# Stop when -1 is entered. 
# Count: 
# • Transactions above ₹50,000  
# • Transactions below ₹1,000  
# • Total transaction amount

# Counters and total amount
count1 = 0
count2 = 0
total_amt = 0

while(True):
    print("-1 for transaction end")
    amount = int(input("Enter amount: "))

    # Reject negative amounts
    if(amount < -1):
        print("Transaction amount cannot be negative")
        continue

    # Stop input
    elif(amount == -1):
        break

    # Count transactions above ₹50,000
    elif(amount > 50000):
        count1 += 1

    # Count transactions below ₹1,000
    elif(amount < 1000):
        count2 += 1

    # Add valid transaction to total
    total_amt += amount

# Display results
print("Transactions above ₹50,000:", count1)
print("Transactions below ₹1,000:", count2)
print("Total transaction amount:", total_amt)