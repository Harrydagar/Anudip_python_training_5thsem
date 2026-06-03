#program to  convert time into corresponding hpor,minutes and second
#input of time in second

second=int(input("Enter time in second: "))
#Cheak is second in negative?
if(second<0):
    exit("Time cannot be in negative.......Exited")
#
hour=0
minutes=0
#---------------Hour-----------------
if(second>=3600):
    hour=second//3600
    second=second%3600
#---------------Minutes-------------
if(second>=60):
    minutes=second//60
    second=second%60
#------------------Output--------------------
print("Exact Time =",hour,":",minutes,":",second)
 
