"""8. Bus Route Monitoring
Problem Statement
Passenger count at each stop:
passengers = [12, 18, 25, 30, 28, 15, 8]
Write a program to:
•
Find the busiest stop.
•
Display stops with fewer than 10 passengers.
•
Calculate average passengers.
•
Determine whether any stop exceeded 25 passengers.
"""

# Passenger count at each stop
passengers = [12, 18, 25, 30, 28, 15, 8]

highest = passengers[0]
total = 0
exceeded = False

for count in passengers:

    if count > highest:
        highest = count

    total += count

    if count > 25:
        exceeded = True

average = total / len(passengers)

print("Busiest Stop Passenger Count:", highest)

print("\nStops With Less Than 10 Passengers:")

for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1)

print("\nAverage Passengers:", average)

if exceeded:
    print("A Stop Exceeded 25 Passengers")
else:
    print("No Stop Exceeded 25 Passengers")