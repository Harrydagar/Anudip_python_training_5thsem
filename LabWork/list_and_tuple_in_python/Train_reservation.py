"""
10. Train Reservation Waiting List
Problem Statement
Passenger records:
passengers = [ ("Anuj", "Confirmed"), ("Rahul", "Waiting"), ("Priya", "Confirmed"), ("Amit", "Waiting"), ("Neha", "Confirmed") ]
Write a program to:
• Display all waiting-list passengers.
• Count confirmed and waiting passengers.
• Find whether a specific passenger has a confirmed ticket.
• Create separate lists for confirmed and waiting passengers."""

# Passenger records
passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

confirmed_count = 0
waiting_count = 0

confirmed_list = []
waiting_list = []

print("Waiting List Passengers:")

for passenger in passengers:

    if passenger[1] == "Waiting":
        print(passenger[0])
        waiting_count += 1
        waiting_list.append(passenger[0])

    else:
        confirmed_count += 1
        confirmed_list.append(passenger[0])

print("\nConfirmed Passengers:", confirmed_count)
print("Waiting Passengers:", waiting_count)

search_name = "Priya"

for passenger in passengers:
    if passenger[0] == search_name and passenger[1] == "Confirmed":
        print("\nConfirmed Ticket Found For:", search_name)
        break

print("\nConfirmed List:", confirmed_list)
print("Waiting List:", waiting_list)