# Problem Statement: 
# Given an amount, determine the minimum number of notes required using: 
# ₹500, ₹200, ₹100, ₹50, ₹20, ₹10

user_amount=int(input("Input:"))
print("Output:")

    
amount=user_amount//500
user_amount=user_amount-amount*500
print("500 x ",amount)


amount=user_amount//200
user_amount=user_amount-amount*200
print("200 x ",amount)


amount=user_amount//100
user_amount=user_amount-amount*100
print("100 x ",amount)

amount=user_amount//50
user_amount=user_amount-amount*50
print("50 x ",amount)

amount=user_amount//20
user_amount=user_amount-amount*20
print("20 x ",amount)

amount=user_amount//10
user_amount=user_amount-amount*10
print("10 x ",amount)

amount=user_amount//2
user_amount=user_amount-amount*2
print("2 x ",amount)

amount=user_amount//1
user_amount=user_amount-amount*1
print("1 x ",amount)