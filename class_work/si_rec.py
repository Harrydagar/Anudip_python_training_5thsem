# Simple Interest and Area/Perimeter Calculator
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (years): "))

if principal <= 0:
    print("Error: Principal amount must be greater than 0.")
elif rate < 0:
    print("Error: Rate of interest cannot be negative.")
elif time <= 0:
    print("Error: Time must be greater than 0.")
else:
    si = (principal * rate * time) / 100
    print("Simple Interest =", si)

# Area and Perimeter of a Rectangle
length = float(input("Enter Length: "))
breadth = float(input("Enter Breadth: "))

if length <= 0:
    print("Error: Length must be greater than 0.")
elif breadth <= 0:
    print("Error: Breadth must be greater than 0.")
else:
    area = length * breadth
    perimeter = 2 * (length + breadth)

    print("Area =", area)
    print("Perimeter =", perimeter)    

# Triangle Validator
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))