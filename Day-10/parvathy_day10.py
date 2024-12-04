'''
Author:Parvathy J Nair
Description: Write a Python program that takes the user's weight (in kilograms)
 and height (in meters),calculates their Body Mass Index (BMI), and displays the result.
'''
weight=float(input("Enter your weight in kg:"))
height=float(input("Enter your height in meters:"))
BMI=weight/(height**2)
print(f"Your BMI is :{BMI}")