# --- Step 1: Initialize the dataset and tracking lists ---
transactions = [5000, -2000, 3000, -1000, -500, 7000]

deposits = []
withdrawals = []

# Initialize max trackers with 0 since we'll evaluate valid amounts
largest_deposit = 0
largest_withdrawal_amount = 0  # Tracking the raw magnitude (absolute size)

# --- Step 2: Loop through and sort transactions ---
for tx in transactions:
    # Positive values are deposits
    if tx > 0:
        deposits.append(tx)
        # Check if it's the biggest deposit seen so far
        if tx > largest_deposit:
            largest_deposit = tx
            
    # Negative values are withdrawals
    elif tx < 0:
        withdrawals.append(tx)
        # Compare raw sizes using abs() so we are looking for the biggest spending jump
        # e.g., spending 2000 is a larger transaction size than spending 500
        if abs(tx) > largest_withdrawal_amount:
            largest_withdrawal_amount = abs(tx)

# --- Step 3: Run overall calculations ---
# Current balance is simply the total sum of all additions and subtractions combined
current_balance = sum(transactions)

# Re-apply the negative sign to our largest tracked withdrawal size to match target output
largest_withdrawal = -largest_withdrawal_amount

# --- Step 4: Display the processed summaries ---
print(f"Current Balance: {current_balance}")
print(f"Deposits: {deposits}")
print(f"Withdrawals: {withdrawals}")
print(f"Largest Deposit: {largest_deposit}")
print(f"Largest Withdrawal: {largest_withdrawal}")