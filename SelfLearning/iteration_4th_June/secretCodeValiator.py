# Problem Statement: 
# A secret code is valid if: 
# • It contains exactly 6 digits.  
# • Sum of first 3 digits equals sum of last 3 digits. 


print("""A secret code is valid if:
It contains exactly 6 digits.
Sum of first 3 digits equals sum of last 3 digits.
""")

user_code = int(input("Input: "))

# Check length
if len(str(user_code)) != 6:
    print("Invalid Code")
    exit("Secret code must contain exactly 6 digits")

sum1 = 0
sum2 = 0

while user_code:
    digit = user_code % 10
    

    if len(str(user_code)) > 3:
        sum2 += digit
    else:
        sum1 += digit

    user_code //= 10

if sum1 == sum2:
    print("Valid Code")
else:
    print("Invalid Code")