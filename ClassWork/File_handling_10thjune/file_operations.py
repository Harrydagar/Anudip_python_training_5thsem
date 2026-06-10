"""Classwork : 
To read the data from file and display the following:

a. No. of Vowels in file.
b. No. of characters into the file.
c. No. of lines into the file.
"""


#To read data from a file
#open a file 
file=open("sentences.txt","r+")
#Taking out content from file to a variable 
content=file.readlines()

print(content)

