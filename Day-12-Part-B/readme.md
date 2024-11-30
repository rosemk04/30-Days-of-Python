Task: Build a Simple Number Guessing Game
Objective: Write a Python program that uses loops and conditionals to create a simple game where the user guesses a randomly generated number.

Instructions:
1.Open your coding environment: Use a code editor, IDE, or Python terminal to write your program.
2.Write the code: Enter the following Python code into your script:

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.")

# Loop to allow the user to guess
while attempts < max_attempts:
    # Get the user's guess
    guess = int(input("Enter your guess: "))
    attempts += 1

    # Check the guess
    if guess == secret_number:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    # Check if attempts are over
    if attempts == max_attempts:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")
        break

3.Run the program: Save and execute the code.
4.Play the game:

The program will generate a random number, and you need to guess it within a limited number of attempts.
Example interaction:
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 attempts to guess it.
Enter your guess: 50
Too low! Try again.
Enter your guess: 75
Too high! Try again.
Enter your guess: 60
Congratulations! You guessed the number 60 in 3 attempts!

Explanation:
random.randint(1, 100): Generates a random number between 1 and 100.
while attempts < max_attempts: Ensures the user has a limited number of attempts.
Conditionals (if-elif-else): Checks if the guess is correct, too low, or too high.
break: Ends the loop if the user guesses correctly or runs out of attempts.
