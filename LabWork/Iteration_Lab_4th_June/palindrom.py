# Palindrome and Reverse Number Checker

# Accept number from user
num = int(input("Enter a number: "))

# Store original number
original_num = num

# Variable to store reversed number
reverse_num = 0

# Reverse the number
while num > 0:
    digit = num % 10              # Extract last digit
    reverse_num = reverse_num * 10 + digit
    num = num // 10               # Remove last digit

# Display reversed number
print("Reverse:", reverse_num)

# Check palindrome
if original_num == reverse_num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")