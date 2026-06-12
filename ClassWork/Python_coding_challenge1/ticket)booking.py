def display_available(tickets):
    print("Available Seats:")

    for seat, status in tickets.items():
        if status == "Available":
            print(seat)


def count_seats(tickets):
    booked = 0
    available = 0

    for status in tickets.values():
        if status == "Booked":
            booked += 1
        else:
            available += 1

    print("\nBooked Seats:", booked)
    print("Available Seats:", available)


def reserve_first_seat(tickets):
    for seat, status in tickets.items():
        if status == "Available":
            tickets[seat] = "Booked"
            print(f"\nSeat {seat} Reserved Successfully.")
            break


def save_tickets(tickets):
    file = open("tickets.txt", "w")

    for seat, status in tickets.items():
        file.write(f"{seat},{status}\n")

    file.close()

    print("\nBooking Details Saved Successfully.")


def occupancy_percentage(tickets):
    booked = list(tickets.values()).count("Booked")

    percentage = (booked / len(tickets)) * 100

    print(f"\nHall Occupancy Percentage: {percentage:.1f}%")


tickets = {
    "A1": "Booked",
    "A2": "Available",
    "A3": "Booked",
    "A4": "Available",
    "B1": "Booked",
    "B2": "Available",
    "B3": "Booked",
    "B4": "Available",
    "C1": "Booked",
    "C2": "Available"
}

display_available(tickets)
count_seats(tickets)
reserve_first_seat(tickets)
occupancy_percentage(tickets)
save_tickets(tickets)