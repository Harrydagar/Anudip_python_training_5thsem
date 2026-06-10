"""
1. Railway Reservation Seat Analyzer
Problem Statement
A railway coach has seats represented as follows:
seats = [ "Booked", "Available", "Booked", "Booked", "Available", "Available", "Booked", "Available", "Booked", "Booked", "Available", "Booked" ]
Requirements
Create the following functions:
1. count_seats(seats)
Returns the number of booked and available seats.
2. first_available(seats)
Returns the seat number of the first available seat.
3. occupancy_percentage(seats)
Returns the percentage of occupied seats.
4. display_available_seats(seats)
Displays all available seat numbers.
Sample Output
Booked Seats: 7 Available Seats: 5 First Available Seat: 2 Occupancy Percentage: 58.33% Available Seat Numbers: 2 5 6 8 11

"""

# Railway Reservation Seat Analyzer

seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# Function to count booked and available seats
def count_seats(seats):
    booked = seats.count("Booked")
    available = seats.count("Available")
    return booked, available

# Function to find first available seat
def first_available(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
            return i + 1      # Seat numbers start from 1
    return -1

# Function to calculate occupancy percentage
def occupancy_percentage(seats):
    booked = seats.count("Booked")
    return (booked / len(seats)) * 100

# Function to display available seat numbers
def display_available_seats(seats):
    print("Available Seat Numbers:", end=" ")
    for i in range(len(seats)):
        if seats[i] == "Available":
            print(i + 1, end=" ")
    print()

# Main Program
booked, available = count_seats(seats)

print("Booked Seats:", booked)
print("Available Seats:", available)
print("First Available Seat:", first_available(seats))
print("Occupancy Percentage:", round(occupancy_percentage(seats), 2), "%")

display_available_seats(seats)