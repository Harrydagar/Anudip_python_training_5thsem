# A website allows users to log in using a password. The correct password is admin123. 
# Write a program that keeps asking the user to enter the password until the correct password is provided.

original_pass="admin123"

while(True):
    user_input=(input("Enter password: "))
    if(user_input=="admin123"):
        print("Login Successful.")
        break
    else:
        print("Invalid Password. .")    