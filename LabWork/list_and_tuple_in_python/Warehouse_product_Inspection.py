"""9. Warehouse Product Inspection
Problem Statement
Product IDs and quality status:
products = [ (101, "Pass"), (102, "Fail"), (103, "Pass"), (104, "Fail"),
(105, "Pass") ]
Write a program to:
•
Display failed product IDs.
•
Count passed and failed products.
•
Calculate pass percentage.
•
Stop checking if 3 failures are found.
"""

# Product ID and quality status
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

passed = 0
failed = 0

print("Failed Product IDs:")

for product in products:

    if product[1] == "Fail":
        print(product[0])
        failed += 1
    else:
        passed += 1

    # Stop if 3 failures are found
    if failed == 3:
        break

pass_percentage = (passed * 100) / (passed + failed)

print("\nPassed Products:", passed)
print("Failed Products:", failed)
print("Pass Percentage:", pass_percentage)