def display_vacant(slots):
    print("\nVacant Parking Slots:")

    for i in range(len(slots)):
        if slots[i] == "Vacant":
            print(i + 1, end=" ")

    print()


def count_slots(slots):
    occupied = slots.count("Occupied")
    vacant = slots.count("Vacant")

    print("\nOccupied Slots:", occupied)
    print("Vacant Slots:", vacant)


def allocate_slot(slots):
    for i in range(len(slots)):
        if slots[i] == "Vacant":
            slots[i] = "Occupied"
            print(f"\nVehicle Allocated to Slot {i+1}")
            return


def occupancy_percentage(slots):
    occupied = slots.count("Occupied")
    total = len(slots)

    percentage = (occupied / total) * 100

    print(f"\nOccupancy Percentage: {percentage:.1f}%")


def save_parking(slots):
    file = open("parking.txt", "w")

    for i in range(len(slots)):
        file.write(f"Slot {i+1} : {slots[i]}\n")

    file.close()

    print("\nParking Details Saved Successfully.")


# Main Program
parking_slots = [
    "Occupied", "Vacant", "Occupied", "Vacant",
    "Occupied", "Occupied", "Vacant", "Occupied",
    "Vacant", "Occupied"
]

display_vacant(parking_slots)
count_slots(parking_slots)
allocate_slot(parking_slots)
occupancy_percentage(parking_slots)
save_parking(parking_slots)