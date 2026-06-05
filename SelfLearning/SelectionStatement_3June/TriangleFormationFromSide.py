#Wap to cheak three side of triangle form a triangle or not

#-------------------------------------------------
print("-----Triangle-----")

side1=float(input("Enter first side (in cm)="))
if(side1<=0):
    exit("Side of triangle should be positive")
#-------------------------------------------------
side2=float(input("Enter first side (in cm)="))
if(side2<=0):
    exit("Side of triangle should be positive")
#-------------------------------------------------
side3=float(input("Enter first side (in cm)="))
if(side3<=0):
    exit("Side of triangle should be positive")
#-------------------------------------------------
#Verifying triangle formation
if(side1+side2>side3 and side2+side3>side1 and side1+side3>side2):
    print("Given sides of triangle form a triangle")
else:
    print("Given sides of triangle do not form a triangle")

#Type of triangle based on side 

if(side1+side2>side3 and side2+side3>side1 and side1+side3>side2):
    
    if(side1==side2==side3):
        print("Equalateral Triangle")
    elif(side1==side2 or side2==side3 or side3==side1):
        print("Isosceles Triangle")
    else:
        print("Scalen Triangle")        

else:
    print("Above angles do not form a triangle")     