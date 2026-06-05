angle1 = float(input("Enter first angle: "))
if angle1 <= 0:
    exit("Angle must be positive")

angle2 = float(input("Enter second angle: "))
if angle2 <= 0:
    exit("Angle must be positive")

angle3 = float(input("Enter third angle: "))
if angle3 <= 0:
    exit("Angle must be positive")

# Verify triangle formation
if angle1 + angle2 + angle3 == 180:
    print("Triangle is valid")

    # Acute angled triangle
    if angle1 < 90 and angle2 < 90 and angle3 < 90:
        print("Triangle formed is an Acute Angled Triangle")

    # Right angled triangle
    elif angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Triangle formed is a Right Angled Triangle")

    # Obtuse angled triangle
    else:
        print("Triangle formed is an Obtuse Angled Triangle")

else:
    print("Triangle is invalid")