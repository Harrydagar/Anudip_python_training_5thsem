# A game has selected a secret number 7. The player must keep guessing the number until the correct guess is made. 
# Write a program that repeatedly asks the user to guess the number and displays a success message when the correct number is 
# entered. 

secret_number=7

while(True):
    user_guess=int(input("Guess the Number:"))
    if(user_guess==secret_number):
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong Guess. Try Again.")    