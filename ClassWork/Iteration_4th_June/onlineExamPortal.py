# Online Exam Portal 
# A student must score at least 40 marks to pass an online assessment. The system allows the student to reattempt the test until 
# the passing score is achieved. 
# Problem Statement: 
# Write a program that accepts marks from the user and continues asking for marks until the entered score is 40 or more. 
# Display a congratulatory message once the student passes the assessment.


while(True):
    user_marks=int(input("Enter Marks:"))
    if(user_marks<0 or user_marks>100):
        print("Invaid marks")
    elif(user_marks>=40):
        print("Result: Pass")
        break
    else:
        print("Result: Fail")

print("Congratulations! You have cleared the assessment.")