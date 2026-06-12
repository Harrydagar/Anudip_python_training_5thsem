# Vehicle Registration Verification System

vehicles = [
    "MH12AB4589", "DL05XY9988", "KA03PQ1234", "UP14CD5678",
    "MH22EF7890", "DL08GH1122", "KA09IJ3344", "UP32KL5566",
    "MH11MN7788", "DL04OP9900", "KA07QR1111", "UP16ST2222",
    "MH15UV3333", "DL09WX4444", "KA10YZ5555", "UP21AA6666",
    "MH20BB7777", "DL02CC8888", "KA05DD9999", "UP18EE0000"
]

state_count = {}
invalid = []

print("VEHICLE REGISTRATION REPORT")
print("-" * 50)

for reg in vehicles:
    state = reg[:2]
    district = reg[2:4]
    series = reg[4:6]
    vehicle_no = reg[6:]

    letters = sum(ch.isalpha() for ch in reg)
    digits = sum(ch.isdigit() for ch in reg)

    valid = (
        len(reg) == 10 and
        reg[:2].isalpha() and
        reg[2:4].isdigit() and
        reg[4:6].isalpha() and
        reg[6:].isdigit()
    )

    print("\nRegistration:", reg)
    print("State Code:", state)
    print("District Code:", district)
    print("Series:", series)
    print("Vehicle Number:", vehicle_no)
    print("Letters:", letters)
    print("Digits:", digits)

    if not valid:
        invalid.append(reg)

    state_count[state] = state_count.get(state, 0) + 1

print("\nINVALID REGISTRATIONS")
if invalid:
    for i in invalid:
        print(i)
else:
    print("No Invalid Registrations")

print("\nSTATE-WISE REPORT")
for state, count in state_count.items():
    print(state, "->", count, "Vehicles")