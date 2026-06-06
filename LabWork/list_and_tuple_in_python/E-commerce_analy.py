"""
1. E-Commerce Order Analysis
Problem Statement
An online store records orders as:
orders = [ ("Laptop", 55000), ("Mouse", 800), ("Keyboard", 1500), ("Monitor", 12000), ("Pen Drive", 600) ]
Write a program to:
•
Display all products costing more than ₹1000.
•
Find the most expensive product.
•
Calculate the total order value.
•
Count products costing below ₹1000."""


# List containing product name and price
orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# Assume first product is the most expensive initially
most_expensive = orders[0]

# Variable to store total order value
total_value = 0

# Counter for products costing below ₹1000
below_1000 = 0

# Display heading
print("-----------------------------------------------------------------------------------------------------")
print("Products costing more than ₹1000:")

# Loop through each order in the list
for item in orders:

    # Check if product price is greater than ₹1000
    if item[1] > 1000:
        print(item[0], "-", item[1])

    # Compare current product price with highest price found so far
    if item[1] > most_expensive[1]:
        most_expensive = item

    # Add current product price to total order value
    total_value = total_value + item[1]

    # Count products costing less than ₹1000
    if item[1] < 1000:
        below_1000 = below_1000 + 1

# Display most expensive product details
print("---------------------------------------------------------------------------------------------------------")
print("\nMost Expensive Product:")
print(most_expensive[0], "-", most_expensive[1])

# Display total value of all orders
print("\nTotal Order Value:", total_value)
print("---------------------------------------------------------------------------------------------------------")

# Display count of products costing below ₹1000
print("\nProducts Costing Below ₹1000:", below_1000)