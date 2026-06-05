#WAP to display grade from given marks.
#------------------------------------------------------------------
#Input marks
marks=float(input("Enter the marks of the student: "))
#------------------------------------------------------------------
#Validation
if(marks<0 or marks>100):
    exit("Invalid marks")
#------------------------------------------------------------------
#displaying grade
if(marks>=90):
    print(" A Grade")
elif(marks>=75):
    print(" B Grade")    
elif(marks>=60):
    print(" C Grade")
elif(marks>=40):
    print(" D Grade")
else:
    print("Fail")        