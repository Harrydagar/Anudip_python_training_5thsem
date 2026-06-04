# A Strong Number is a number whose sum of factorials of digits equals the number itself. 
# Write a program to check whether a given number is a Strong Number.

user_input=int(input("Input:"))
og=user_input
fact=1
sum=0
while(user_input>0):
    num=user_input%10
    for i in range(1,num+1):
        fact*=i
    sum+=fact
    user_input=user_input//10
    fact=1
    

if(sum==og):
    print("Output:")
    print(og,"is an strong Number")
else:   
    print("Output:")
    print(og,"is not an strong Number") 