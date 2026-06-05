# Lift Movement Simulation 

# Lift starts from floor 0
current_floor = 0
total_travelled = 0

while True:

    # Take destination floor from user
    destination = int(input("Enter Destination (-1 to stop): "))

    # Stop the program if user enters -1
    if destination == -1:
        break

    # Calculate floors travelled
    if destination > current_floor:
        travelled = destination - current_floor
    else:
        travelled = current_floor - destination

    # Display floors travelled in this trip
    print("Travelled:", travelled, "floors")

    # Add to total travelled floors
    total_travelled += travelled

    # Update current floor
    current_floor = destination

# Display total floors travelled
print("Total Travelled:", total_travelled, "floors")