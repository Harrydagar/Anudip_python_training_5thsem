#Program to CALCULATE AREA AND PARAMETER OF TRIANGLE
#Input of three sides
print("-----Triangle-----")
side1=float(input("Enter first side (in cm)="))
side2=float(input("Enter first side (in cm)="))
side3=float(input("Enter first side (in cm)="))
#-------------------------------------------------
print("-----------------------")
print("First Side :",side1,"cm")
print("Second Side :",side2,"cm")
print("Third Side :",side3,"cm")
#-------------------------------------------------
parameter=side1+side2+side3
#Need to calculate Area
s=(side1+side2+side3)/2
#-------------------------------------------------
print("Area of the Triangle is:",(s*(s-side1)*(s-side2)*(s-side3))**(1/2),"sq.cm")
print("Parameter of the Triangle is:",parameter,"cm")