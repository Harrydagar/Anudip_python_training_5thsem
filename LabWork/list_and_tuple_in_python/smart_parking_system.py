"""
3. Smart Parking System
Problem Statement
Parking slots are represented as:
slots = [1, 0, 1, 1, 0, 0, 1, 0]
Where:
•
1 = Occupied
• 0 = Available
Write a program to:
• Count occupied and available slots.
• Find the first available slot.
• Display all available slot numbers.
• Check whether parking occupancy exceeds 75%."""

# Parking slot status
slots = [1, 0, 1, 1, 0, 0, 1, 0]

occupied = 0
available = 0

available_slots = []

# Count occupied and available slots
for i in range(len(slots)):

    if slots[i] == 1:
        occupied += 1
    else:
        available += 1
        available_slots.append(i + 1)

# Find first available slot
for i in range(len(slots)):
    if slots[i] == 0:
        first_available = i + 1
        break

# Calculate occupancy percentage
occupancy = (occupied * 100) / len(slots)
print("---------------------------------------------------------------------------------------------------------")
print("Occupied Slots:", occupied)
print("Available Slots:", available)
print("First Available Slot:", first_available)
print("---------------------------------------------------------------------------------------------------------")
print("Available Slot Numbers:", available_slots)
print("Occupancy Percentage:", occupancy)
print("---------------------------------------------------------------------------------------------------------")

if occupancy > 75:
    print("Parking Occupancy Exceeds 75%")
else:
    print("Parking Occupancy Does Not Exceed 75%")
    