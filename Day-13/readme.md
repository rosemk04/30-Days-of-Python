Task: Check Whether a Given Year is a Leap Year
Objective: Write a Python program that checks if a given year is a leap year.

Instructions:
1.Open your coding environment: Use a code editor, IDE, or Python terminal to write your program.
2.Write the code: Enter the following Python code into your script:

# Ask the user to enter a year
year = int(input("Enter a year to check if it's a leap year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
3.Run the program: Save and execute the code.
4.Test the program:

Enter different years to see the output.
Example interaction:

Enter a year to check if it's a leap year: 2024
2024 is a leap year.
Enter a year to check if it's a leap year: 1900
1900 is not a leap year.

Explanation:
Leap Year Rules:
A year is a leap year if it is divisible by 4 and not divisible by 100, or if it is divisible by 400.
Conditionals:
year % 4 == 0: Checks if the year is divisible by 4.
year % 100 != 0: Ensures it is not a century year (except divisible by 400).
year % 400 == 0: Century years must also be divisible by 400 to be leap years.
