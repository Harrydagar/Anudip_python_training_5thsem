#Program to cheak three angles form a triangle or not
#-------------------------------------------------------------  
angle1=float(input("Enter first angle: "))
#Validate angle1
if angle1<=0:
    exit("Angle must be positive")
#-------------------------------------------------------------
angle2=float(input("Enter second angle: "))
#Validate angle2
if angle2<=0:
    exit("Angle must be positive")   
#-------------------------------------------------------------
angle3=float(input("Enter third angle: "))
#Validate angle3
if angle3<=0:
    exit("Angle must be positive")         
#-------------------------------------------------------------
#Verifying triangle formation

if(angle1+angle2+angle3 ==180):
    print("Above angles form a triangle")
else:
    print("Above angles do not form a triangles")    


#Specifies type of triangle

if(angle1 + angle2 + angle3 == 180):
    # Type by angles
    if(angle1 == 90 or angle2 == 90 or angle3 == 90):
        print("Right Angle Triangle")

    elif(angle1 > 90 or angle2 > 90 or angle3 > 90):
        print("Obtuse Triangle")

    else:
        print("Acute Triangle")

else:
    print("Above angles do not form a triangle") 
