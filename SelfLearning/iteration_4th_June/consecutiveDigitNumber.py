# Accept a number and check whether every digit is exactly 1 greater
# than the previous digit (e.g., 1234, 4567)

# Input from user
user_input = int(input("Input: "))

# Store the last digit
temp = user_input % 10

# Difference counter
i = 1

# Flag to track whether number is consecutive
flag = 0

# Check digits one by one from right to left
while(user_input):

    # Remove the last digit
    user_input = user_input // 10

    # Get the new last digit
    temp2 = user_input % 10

    # Stop when no more digits are left
    if(user_input == 0):
        break

    # Check if current digit is i less than previous digit
    if(temp == temp2 + i):
        i += 1      # Increase expected difference
        flag = 1
    else:
        flag = 0
        break

# Display result
if(flag == 1):
    print("Output: Consecutive Number")
else:
    print("Output: Not a Consecutive Number")