# WAP for displaying battery charging levell

charging_level = int(input("Enter your current battery level: "))

if charging_level < 0:
    print("Battery charging level cannot be negative")
    exit()

electricity_status = True

while charging_level < 100:
    if electricity_status:
        print("Battery Level:", charging_level, "%")
        charging_level += 10

        if charging_level > 100:
            charging_level = 100
    else:
        break

print("Battery Level:", charging_level, "%")
print("Full charge")