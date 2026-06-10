"""
2. Food Delivery Performance Tracker
Problem Statement
Delivery times (in minutes) for different orders are given below:
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]
Requirements
Create the following functions:
1. fastest_delivery(times)
Returns the shortest delivery time.
2. delayed_orders(times)
Returns a list of orders taking more than 45 minutes.
3. average_delivery_time(times)
Returns the average delivery time.
4. delivery_category(times)
Displays order categories:
•
Fast → ≤ 30 minutes
•
Normal → 31–45 minutes
•
Delayed → > 45 minutes
Sample Output
Fastest Delivery: 18 minutes Delayed Orders: [60, 80, 55] Average Delivery Time: 40.8 minutes Categories: 28 -> Fast 45 -> Normal 60 -> Delayed"""

# Food Delivery Performance Tracker

delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# Function to find fastest delivery
def fastest_delivery(times):
    return min(times)

# Function to return delayed orders
def delayed_orders(times):
    delayed = []
    for time in times:
        if time > 45:
            delayed.append(time)
    return delayed

# Function to calculate average delivery time
def average_delivery_time(times):
    return sum(times) / len(times)

# Function to display categories
def delivery_category(times):
    print("Categories:")
    
    for time in times:
        if time <= 30:
            category = "Fast"
        elif time <= 45:
            category = "Normal"
        else:
            category = "Delayed"
            
        print(time, "->", category)

# Main Program
print("Fastest Delivery:", fastest_delivery(delivery_time), "minutes")
print("Delayed Orders:", delayed_orders(delivery_time))
print("Average Delivery Time:", round(average_delivery_time(delivery_time), 2), "minutes")

delivery_category(delivery_time)