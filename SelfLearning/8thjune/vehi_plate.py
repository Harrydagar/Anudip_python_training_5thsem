plate = "MH12AB4589"

state = plate[:2]
district = plate[2:4]
series = plate[4:6]
number = plate[6:]

letters = 0
digits = 0

for ch in plate:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

valid = True

if not (state.isalpha() and district.isdigit() and series.isalpha() and number.isdigit()):
    valid = False

print("State Code:", state)
print("District Code:", district)
print("Series:", series)
print("Vehicle Number:", number)
print("Total Letters:", letters)
print("Total Digits:", digits)

if valid:
    print("Vehicle Number Status: Valid")
else:
    print("Vehicle Number Status: Invalid")