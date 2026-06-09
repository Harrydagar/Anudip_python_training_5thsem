#Wap to calculate area and parameter of a rectangle 


#----------------Length-----------------------
length = float(input("Enter length (cm): "))
if(length <=0 ):
    exit("Length must be > 0")
#----------------Breadth-----------------------
breadth = float(input("Enter breadth (cm): "))
if(breadth <=0 ):
    exit("Breadth must be > 0")
#------------------Inputs------------------------
print("Length=",length)
print("Breadth=",breadth)
#----------Area and parimeter--------------
area = length * breadth
perimeter = 2 * (length + breadth)

print(f"Area = {area:.2f} cm²")
print(f"Perimeter = {perimeter:.2f} cm")