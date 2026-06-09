#WAP to calculate Simple Interest 
print("-----------Simple Interest--------------")

principle=float(input("Enter principle amount: "))
if(principle<=0):
    exit("Invalid input... Exited")

rate=float(input("Enter rate(%): "))
if(rate<0):
    exit("Invalid input... Exited")

time=int(input("Enter Time(in years)"))
if(time<0):
    exit("Invalid input... Exited")
#----------------Print-----------------------
print("Principle=",principle)
print("Rate=",rate)
print("Time=",time)


print("Simple Interest =₹",(principle*rate*time)/100)