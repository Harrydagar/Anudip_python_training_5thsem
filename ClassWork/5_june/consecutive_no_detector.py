# --- Step 1: Initialize the dataset and pair tracker ---
numbers = [4, 5, 6, 10, 11, 15, 16, 17]
consecutive_pairs = []

# --- Step 2: Loop through the list using index positions ---
# We stop at 'len(numbers) - 1' so that when we stand on the second-to-last item,
# looking ahead doesn't throw an "IndexOutOfBounds" crash error on the last item.
for i in range(len(numbers) - 1):
    
    current_num = numbers[i]
    next_num = numbers[i + 1]
    
    # Check if the next number is exactly 1 unit greater than the current number
    if next_num == current_num + 1:
        # Print the live text match to the console
        print(f"{current_num} and {next_num} are consecutive")
        
        # Save the match as a pair (tuple) inside our tracking list
        consecutive_pairs.append((current_num, next_num))

# --- Step 3: Print the collected list of pairs ---
print("\n--- Additional Challenge Pair List ---")
print(consecutive_pairs)