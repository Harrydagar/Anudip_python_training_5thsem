# main.py
# Program to use geometry module

import geometry

print("----- 2D SHAPE CALCULATOR -----")

print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")

choice = int(input("Enter your choice: "))

# ---------------- CIRCLE ----------------
if choice == 1:
    r = float(input("Enter radius: "))
    print("Area of Circle:", geometry.circle_area(r))
    print("Perimeter of Circle:", geometry.circle_perimeter(r))

# ---------------- RECTANGLE ----------------
elif choice == 2:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    print("Area of Rectangle:", geometry.rectangle_area(l, b))
    print("Perimeter of Rectangle:", geometry.rectangle_perimeter(l, b))

# ---------------- SQUARE ----------------
elif choice == 3:
    s = float(input("Enter side: "))
    print("Area of Square:", geometry.square_area(s))
    print("Perimeter of Square:", geometry.square_perimeter(s))

# ---------------- TRIANGLE ----------------
elif choice == 4:
    a = float(input("Enter side A: "))
    b = float(input("Enter side B: "))
    c = float(input("Enter side C: "))
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))

    print("Area of Triangle:", geometry.triangle_area(base, height))
    print("Perimeter of Triangle:", geometry.triangle_perimeter(a, b, c))

else:
    print("Invalid choice")