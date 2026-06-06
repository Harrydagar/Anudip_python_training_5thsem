# A water tank is being filled with water at a constant rate of 10 liters per minute. Initially, the tank contains 0 liters of water. 
# Write a program that displays the amount of water in the tank after each minute and continues until the tank reaches 100 liters. 

current_filled=0

while(current_filled<=100):
    print("WATER FILLED: ",current_filled)
    current_filled+=10

print("Tank is Full")