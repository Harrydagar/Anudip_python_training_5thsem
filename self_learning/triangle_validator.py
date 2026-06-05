# Triangle Validator
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Error: All sides must be greater than 0.")
else:
    if (side1 + side2 > side3) and \
       (side1 + side3 > side2) and \
       (side2 + side3 > side1):
        print("The given sides form a triangle.")
    else:
        print("The given sides do not form a triangle.")
