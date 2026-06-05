# Problem Statement: 
# Accept a number from the user and determine whether it is a prime number or not. 
# Additional Requirement: 
# If the number is not prime, display all its factors. 

user_input=int(input("Input:"))
count=0
#Cheaking 0 and -ve conditions
if(user_input<=1):
    exit("Prime no are greater than 1")
#Prime no logic
else: 
    print("Output:")
    print("Factor:",end="")
    for i in range(1,(user_input//2)+1):
        if(user_input%i==0):
            print(i,end=" ")
            count+=1
    print(user_input)
if(count==2):
    print(user_input,"is a Prime Number") 
else:
    print(user_input,"is not a Prime Number")
           






        
    
