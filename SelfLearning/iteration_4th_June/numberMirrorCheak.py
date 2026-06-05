# Problem Statement: 
#  Checkwhether the left half of a number is identical to the right half.


user_input=int(input("Input:"))

#counts digit
temp=user_input
digit=0

#To get number of digit
while(temp%10!=0):
    digit+=1
    temp//=10

#To cheak no of digit must b even
if(digit%2!=0):
    print("Not a Mirror Number")

else:   
    power=1 
    half = digit // 2 

    for i in range(half):
        power*=10

    right=user_input % power    #Right half  
    left=user_input // power    #Left half

    if(right==left):
        print("Output: Mirror Number ")

    else:
        print("Output: Not Mirror Number ")



