emp = "EMP2026ANUJ458"

upper = 0
digits = 0
digit_list = []

for ch in emp:
    if ch.isupper():
        upper += 1
    if ch.isdigit():
        digits += 1
        digit_list.append(int(ch))

year = emp[3:7]
name = emp[7:-3]

valid = True

if emp[:3] != "EMP":
    valid = False
if len(year) != 4:
    valid = False
if len(emp[-3:]) != 3:
    valid = False

sum_digits = 0
for d in digit_list:
    sum_digits += d

print("Uppercase Letters:", upper)
print("Digits:", digits)
print("Joining Year:", year)
print("Employee Name:", name)
print("Digit List:", digit_list)
print("Sum of Digits:", sum_digits)

if valid:
    print("ID Status: Valid")
else:
    print("ID Status: Invalid")