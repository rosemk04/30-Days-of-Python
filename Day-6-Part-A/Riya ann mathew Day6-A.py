'''Author:Riya ann mathew
Description:Task: Write a Python program to display the first 10 numbers of a multiplication table for a number chosen by the user.

'''
number=int(input("Enter the number:"))
for i in range(1,11):
    Result=number*(i)
    print(i,"*","=",Result)