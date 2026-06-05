# --- Step 1: Initialize the dataset and tracking variables ---
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

booked_count = 0
available_count = 0

available_seat_numbers = []
first_available_seat = None

# --- Step 2: Loop through seats tracking both index and booking status ---
for index, status in enumerate(seats):
    # Convert computer 0-index to human seat numbering (Seat 1, Seat 2, etc.)
    seat_number = index + 1
    
    # 1. Evaluate booking status
    if status == 1:
        booked_count += 1
    elif status == 0:
        available_count += 1
        available_seat_numbers.append(seat_number)
        
        # 2. Capture the very first available seat and lock it in
        if first_available_seat is None:
            first_available_seat = seat_number

# --- Step 3: Calculate the occupancy percentage ---
total_seats = len(seats)
occupancy_percentage = (booked_count / total_seats) * 100

# Determine if the bus is overcrowded (exceeds 70%)
if occupancy_percentage > 70:
    occupancy_status = "More Than 70% Occupied"
else:
    occupancy_status = "Not More Than 70% Occupied"

# --- Step 4: Display the reservation metrics ---
print(f"Booked Seats: {booked_count}")
print(f"Available Seats: {available_count}")
print(f"First Available Seat: {first_available_seat}")
print(f"Available Seat Numbers: {available_seat_numbers}")
print(f"Bus Occupancy: {occupancy_percentage:.0f}%")
print(f"Status: {occupancy_status}")