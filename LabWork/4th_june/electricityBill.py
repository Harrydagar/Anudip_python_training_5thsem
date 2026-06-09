# Electricity Bill Calculator using Slab Rates

# units consumed
units = int(input("Enter Electricity Unit: "))

# Validation
if units < 0:
    exit("Units can't be negative")

#Bill calc


if units <= 100:
    bill = units * 5
    category = "Low"

#Now starting 100 unit calc as 5 rs and next with 7 rs
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
    category = "Medium"
#Same logic here start 100*5 then next 100*7 then other *10
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    category = "High"

# Output

print("\n----- Electricity Bill -----")
print("Units Consumed :", units)
print("Total Bill : ₹", bill)
print("Category :", category)




