# Problem Statement: 
# Input lap times of N racers. 
# Display: 
# • Fastest racer position  
# • Slowest racer position  
# • Difference between fastest and slowest lap time 


# Number of racers
n = int(input("Enter number of racers: "))

# First racer's time
lap_time = float(input("Lap time of Racer 1: "))

# Initial values
fastest = lap_time
slowest = lap_time
fastest_pos = 1
slowest_pos = 1

# Check remaining racers
for i in range(2, n + 1):
    lap_time = float(input(f"Lap time of Racer {i}: "))

    # Update fastest
    if lap_time < fastest:
        fastest = lap_time
        fastest_pos = i

    # Update slowest
    if lap_time > slowest:
        slowest = lap_time
        slowest_pos = i

# Time difference
difference = slowest - fastest

# Output
print("\nFastest Racer Position:", fastest_pos)
print("Slowest Racer Position:", slowest_pos)
print("Difference:", difference)