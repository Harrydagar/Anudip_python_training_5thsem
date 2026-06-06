# Flight booking records stored in tuple
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

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

print("Passengers Travelling to Delhi:", delhi_count)

print("Confirmed:", confirmed)
print("Waiting:", waiting)
print("Cancelled:", cancelled)

print("Waiting List:")
print(waiting_list)

# Find destination with highest bookings
if delhi > mumbai and delhi > chennai:
    most_booked = "Delhi"
elif mumbai > chennai:
    most_booked = "Mumbai"
else:
    most_booked = "Chennai"

print("Most Booked Destination:")
print(most_booked)
