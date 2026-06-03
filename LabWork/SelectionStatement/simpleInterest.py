#WAP to calculate Simple Interest 
print("-----------Simple Interest--------------")
principle=float(input("Enter principle amount: "))
rate=float(input("Enter rate(%): "))
time=float(input("Enter Time(in years)"))
#----------------Print-----------------------
print("Principle=",principle)
print("Rate=",rate)
print("Time=",time)
#------------Validation----------------------
if(principle<=0 or rate<0 or time<0):
    exit("Invalid input... Exited")

print("Simple Interest =₹",(principle*rate*time)/100)