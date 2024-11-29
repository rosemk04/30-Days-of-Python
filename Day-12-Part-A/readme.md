Task: Calculate the Factorial of a Number Using Recursion
Objective: Write a Python program that uses recursion to calculate the factorial of a given number.

Instructions:
1.Open your coding environment: Use a code editor, IDE, or Python terminal to write your program.
2.Write the code: Enter the following Python code into your script:

# Define a recursive function to calculate the factorial
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

# Ask the user to enter a number
number = int(input("Enter a number to calculate its factorial: "))

# Ensure the input is non-negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate and display the factorial
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")

3.Run the program: Save and execute the code.
4.Test the program:

Enter a positive number (e.g., 5). The output will be
Enter a number to calculate its factorial: 5  
The factorial of 5 is: 120

Enter 0 or 1. The output will be:
Enter a number to calculate its factorial: 0  
The factorial of 0 is: 1
Enter a negative number. The program will display an error message.

Explanation:
Recursive Function: The factorial function calls itself with a smaller value (n - 1) until the base case (n == 0 or n == 1) is reached.
Base Case: Stops recursion when the input is 0 or 1, returning 1.
n * factorial(n - 1): Multiplies the current number by the factorial of the previous number.
Input Validation: Ensures the user enters a non-negative number.
