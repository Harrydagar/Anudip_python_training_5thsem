"""
Question 2: Flight Booking Analysis
Problem Statement
A flight reservation system stores passenger records as tuples:
bookings = ( ("P101", "Delhi", "Confirmed"), ("P102", "Mumbai", "Waiting"), ("P103", "Delhi", "Confirmed"), ("P104", "Chennai", "Cancelled"), ("P105", "Mumbai", "Confirmed"), ("P106", "Delhi", "Waiting") )
Where:
• Passenger ID
• Destination
• Booking Status
Tasks
Write a Python program to:
1. Display all passengers whose booking status is Confirmed.
2. Count the number of passengers travelling to Delhi.
3. Count Confirmed, Waiting, and Cancelled bookings separately.
4. Create a list containing passenger IDs with Waiting status.
5. Determine which destination has the highest number of bookings."""


# Flight booking records stored in tuple
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)
print("----------------------------------------------------------------")

print("Confirmed Passengers:")

# Initialize counters and lists
delhi_count = 0
confirmed = 0
waiting = 0
cancelled = 0

waiting_list = []

# Destination counters
delhi = 0
mumbai = 0
chennai = 0

# Process booking records
for booking in bookings:

    # Display confirmed passengers
    if booking[2] == "Confirmed":
        print(booking[0], booking[1])
        confirmed += 1

    # Count waiting bookings
    elif booking[2] == "Waiting":
        waiting += 1
        waiting_list.append(booking[0])

    # Count cancelled bookings
    elif booking[2] == "Cancelled":
        cancelled += 1

    # Count bookings by destination
    if booking[1] == "Delhi":
        delhi_count += 1
        delhi += 1

    elif booking[1] == "Mumbai":
        mumbai += 1

    elif booking[1] == "Chennai":
        chennai += 1
print("----------------------------------------------------------------")
print("Passengers Travelling to Delhi:", delhi_count)
print("----------------------------------------------------------------")

print("Confirmed:", confirmed)
print("Waiting:", waiting)
print("Cancelled:", cancelled)
print("----------------------------------------------------------------")
print("Waiting List:")
print(waiting_list)
print("----------------------------------------------------------------")
# Find destination with highest bookings
if delhi > mumbai and delhi > chennai:
    most_booked = "Delhi"
elif mumbai > chennai:
    most_booked = "Mumbai"
else:
    most_booked = "Chennai"

print("Most Booked Destination:")
print(most_booked)
