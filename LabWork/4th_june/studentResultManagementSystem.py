# Problem Statement: 
# Accept marks of 5 subjects. 
# Display: 
# • Total Marks  
# • Percentage  
# • Grade  
# Grade Criteria: 
# Percentage Grade 
# >=90 A+ 
# >=75 A 
# >=60 B 
# >=40 C 
# <40 Fail

sub1=float(input("Enter marks of Subject1:"))
#Validation
if(sub1<0 or sub1>100):
    exit("Subject marks can not be in negative or >100")
sub2=float(input("Enter marks of Subject2:"))
#Validation
if(sub2<0 or sub2>100):
    exit("Subject marks can not be in negative or >100")
sub3=float(input("Enter marks of Subject3:"))
#Validation
if(sub3<0 or sub3>100):
    exit("Subject marks can not be in negative or >100")
sub4=float(input("Enter marks of Subject4:"))
#Validation
if(sub4<0 or sub4>100):
    exit("Subject marks can not be in negative or >100")
sub5=float(input("Enter marks of Subject5:"))
#Validation
if(sub5<0 or sub5>100):
    exit("Subject marks can not be in negative or >100")

total_marks=sub1+sub2+sub3+sub4+sub5
percentage_total=(total_marks/500)*100
print("Total marks:",total_marks)
print("Percentage:",percentage_total)

#Finding Grade
if(percentage_total>=90):
    print("A+")
elif(percentage_total>=75):
    print("A")  
elif(percentage_total>=60):  
    print("B")
elif(percentage_total>=40):  
    print("C")  
else:
    print("Fail")      