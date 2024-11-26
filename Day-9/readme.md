Task: Password Verification Program
Objective: Write a Python program that asks the user to enter a password. If the entered password matches a predefined password, print "Access granted"; otherwise, print "Access denied."

Instructions:
1.Open your coding environment: Use a code editor, IDE, or Python terminal to write your program.
2.Write the code: Enter the following Python code into your script:
# Define the predefined password
predefined_password = "secure123"

# Ask the user to enter a password
user_password = input("Enter your password: ")

# Check if the entered password matches the predefined password
if user_password == predefined_password:
    print("Access granted")
else:
    print("Access denied")

3.Run the program: Save and execute the code.
4.Test the program:
Enter the correct password (secure123). The program should output:
Enter your password: secure123  
Access granted
Enter an incorrect password (e.g., password). The program should output:
Enter your password: password  
Access denied

Explanation:
predefined_password: Stores the password that the program will verify against.
input(): Collects the password entered by the user.
if-else Statement: Compares the user's input with the predefined password. If they match, "Access granted" is printed; otherwise, "Access denied" is displayed.
