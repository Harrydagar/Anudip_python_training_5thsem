# Generate a secret number between 1 and 50. 
# Allow the user to keep guessing until the correct number is found. 
# Display: 
# • "Too High"  
# • "Too Low"  
# • "Correct Guess"  
# Also display the total number of attempts.


secret=8
total_attemt=0
while(True):
    user_input=int(input("Guess a number between(1-50)->"))
    if(user_input>secret):
        total_attemt+=1
        print("Too High")
        print("Total attempt:",total_attemt)
    elif(user_input<secret):
        total_attemt+=1
        print("Too Low")
        print("Total attempt:",total_attemt)
    else:
        total_attemt+=1
        print("Correct Guess")     
        print("Total attempt:",total_attemt)  
        break
