import math

try:
    # Input sides of triangle
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))

    # Check for positive sides
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Triangle sides must be greater than zero.")

    # Check Triangle Inequality Theorem
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("Invalid triangle. The given sides cannot form a triangle.")

    # Heron's Formula
    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print(f"\nArea of Triangle = {area:.2f} square units")

except ValueError as e:
    print("\nError:", e)

except Exception:
    print("\nError: Please enter numeric values only.")

finally:
    print("\nTriangle area calculation process completed.")