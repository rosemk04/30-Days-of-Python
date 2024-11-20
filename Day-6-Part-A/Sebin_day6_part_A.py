'''AUTHOR=SEBIN PRINCE
DESCRIPTION=Print the First 10 Numbers in a Multiplication Table of Your Choice Objective: Write a Python program to display the first 10 numbers of a multiplication table for a number chosen by the user.
'''
a=int(input("Enter the number:"))
b=int(input("Enter the limit"))
c=1
for c in range(1,b+1):
    print(c,"*",a,"=",c*a)
