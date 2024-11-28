'''AUTHOR:SEBIN PRINCE
DESCRIPTION:Calculate BMI Based on User's Weight and Height
Objective: Write a Python program that takes the user's weight (in kilograms) and height (in meters), calculates their Body Mass Index (BMI), and displays the result.
'''
height=float(input("Enter your weight in kg:"))
weight=float(input("E.nter your height in meter:"))
bmi=height/(weight**2)
print("Your BMI is",bmi)
