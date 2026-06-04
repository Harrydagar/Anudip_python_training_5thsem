#A teacher recording student attendence the strength of calss 30 every time they need to insert student is present or absent so count the total no of student is present as wel as absent

student_count=1
present_count=0
absent_count=0
while(student_count<=30):
    attendence=input("Say yes/no: ").lower()
    if(attendence=="yes"):
        print("Student",student_count)
        print("Attendence:","Present")
        present_count+=1
        student_count+=1
    elif(attendence=="no"):
        print("Student",student_count)
        print("Attendence:" "Absent")
        absent_count+=1
        student_count+=1
    else:
        print("Wrong input! Enter only yes or no.") 

print("Total Present:",present_count)
print("Total absent:",absent_count)           