'''
Author:Parvathy J Nair
Description:Write a Python program that asks the user for their birth year,
calculates their age, and displays it
'''

from datetime import datetime
current_year=datetime.now().year
birth_year=int(input("Enter your birth year:"))
age=current_year-birth_year
print(f"You are {age} years old")
