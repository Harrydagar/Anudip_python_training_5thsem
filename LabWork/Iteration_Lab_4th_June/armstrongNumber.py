
# Accept a number from the user and check whether it is an Armstrong Number.
user_input=int(input("Input:"))
#og=original
og=user_input
power=len(str(user_input))
sum=0
#cheaking Armstrong
while(user_input>0):
    num=user_input%10
    sum+=num**power
    user_input=user_input//10
    

if(sum==og):
    print("Output:")
    print(og,"is an Armstrong Number")
else:   
    print("Output:")
    print(og,"is not an Armstrong Number") 
