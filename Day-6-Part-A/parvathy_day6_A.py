'''
Author:Parvathy J Nair
Description:Write a Python program to display the
first 10 numbers of a multiplication table for a
number chosen by the user
'''

number=int(input("Enter a number:"))
print(f"Multiplication table of {number}:")
for i in range(1,11):
    result=number*i
    print(f"{number}*{i}={result}")