# Electricity Bill Calculator using Slab Rates

units = int(input("Enter Electricity Unit: "))

# Validation
if units < 0:
    exit("Units can't be negative")

# Bill calculation
if units <= 100:
    bill = units * 5
    category = "Low"

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
    category = "Medium"

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    category = "High"

# 10% surcharge if bill > 5000
if bill > 5000:
    bill += bill * 0.10

# Output
print("Final Payable Amount: ₹", bill)