'''AUTHOR:SEBIN PRINCE
DESCRIPTION:Calculate the User's Age Based on Their Birth Year Objective: Write a Python program that asks the user for their birth year, calculates their age, and displays it.
'''
from datetime import datetime
current_year=datetime.now().year
a=int(input("Enter your birth year:"))
age=current_year-a
print("You are",age,"years old")
