def display_available(seats):
    print("\nAvailable Seats:")
    for seat, status in seats.items():
        if status == "Available":
            print(seat, end=" ")
    print()


def count_seats(seats):
    booked = 0
    available = 0

    for status in seats.values():
        if status == "Booked":
            booked += 1
        else:
            available += 1

    print("\nBooked Seats:", booked)
    print("Available Seats:", available)


def reserve_first_available(seats):
    for seat, status in seats.items():
        if status == "Available":
            seats[seat] = "Booked"
            print(f"\nSeat {seat} Reserved Successfully.")
            return


def cancel_booking(seats, seat_no):
    if seat_no in seats and seats[seat_no] == "Booked":
        seats[seat_no] = "Available"
        print(f"Seat {seat_no} Booking Cancelled.")
    else:
        print("Invalid Seat Number or Already Available.")


def occupancy_percentage(seats):
    booked = list(seats.values()).count("Booked")
    total = len(seats)

    percentage = (booked / total) * 100
    print(f"\nOccupancy Percentage: {percentage:.1f}%")


def save_reservations(seats):
    file = open("reservations.txt", "w")

    for seat, status in seats.items():
        file.write(f"{seat},{status}\n")

    file.close()
    print("\nReservation Details Saved Successfully.")


# Main Program
seats = {
    1: "Booked",
    2: "Available",
    3: "Booked",
    4: "Available",
    5: "Booked",
    6: "Booked",
    7: "Available",
    8: "Booked",
    9: "Available",
    10: "Booked"
}

display_available(seats)
count_seats(seats)
reserve_first_available(seats)

seat_no = int(input("\nEnter Seat Number to Cancel Booking: "))
cancel_booking(seats, seat_no)

occupancy_percentage(seats)
save_reservations(seats)