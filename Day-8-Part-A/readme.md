Task: Calculate the User's Age Based on Their Birth Year
Objective: Write a Python program that asks the user for their birth year, calculates their age, and displays it.

Instructions:
1.Open your coding environment: Use a code editor, IDE, or Python terminal to write your program.
2.Write the code: Enter the following Python code into your script:

# Ask the user for their birth year
birth_year = int(input("Enter your birth year: "))
# Calculate the current year
import datetime
current_year = datetime.datetime.now().year
# Calculate the user's age
age = current_year - birth_year
# Display the age
print("You are",age,"years old")

3.Run the program: Save and execute the code.
4.Test the program:

Enter your birth year (e.g., 2000).
The program should output something like:
Enter your birth year: 2000  
You are 24 years old.

Explanation:
int(input()): Collects the birth year as an integer.
datetime.datetime.now().year: Gets the current year from the system.
Age Calculation: Subtracts the birth year from the current year to calculate the age.
print(): Displays the calculated age in a formatted message.
