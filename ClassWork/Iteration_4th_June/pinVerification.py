# An ATM machine requires the user to enter the correct PIN to access their account. The valid PIN is 1234. 
# Write a program that repeatedly asks the user to enter a PIN until the correct PIN is entered. 

original_pass=1234

while(True):
    user_input=int(input("Enter Pin: "))
    if(len(user_input)>4 or len(user_input)<4):
        print("Pin must be of length 4")
    if(user_input==1234):
        print("Access Granted.")
        break
    else:
        print("Incorrect PIN. Try Again.")    