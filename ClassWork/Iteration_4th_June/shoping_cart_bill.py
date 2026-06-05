# A customer is adding items to a shopping cart. The price of each item is entered one by one. 
# Write a program that continuously accepts item prices and calculates the total bill amount. The program should stop accepting prices when the user enters 0. 

total_bill=0
while(True):
    item_price=int(input("Enter Item Price:"))
    if(item_price<0):
        print("Price can't be negative")
    elif(item_price==0):
        break
    else:
        total_bill+=item_price

print("Total bill Amount:₹",total_bill)        
    

