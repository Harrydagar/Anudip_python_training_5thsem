# Problem Statement: 
# Accept the number of rows and print the following pattern: 
# For Input: 
# 5 
# Output: 
# 1 
# 12 
# 123 
# 1234 
# 12345 
# Challenge: 
# Print the reverse pattern as well.

#Input from user
pattern_row=int(input("Enter the no of row for pattern:"))
#Validation
if(pattern_row<0):
    exit("Negative number not allowed:")

#Pattern
for i in range(1,pattern_row+1):
    for j in range(1,i+1):
        print(j,end="")
    print()    

# Print the reverse pattern as well.

print()
print("-----------Its reverse-----------")
for i in range(pattern_row,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()    