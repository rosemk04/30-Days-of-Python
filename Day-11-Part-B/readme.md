Task: Find the Sum and Average of Numbers in a List
Instructions:
1.Ask the user to input 5 numbers, one at a time, and store them in a list.
2.Calculate and print the sum of all numbers in the list.
3.Calculate and print the average of the numbers.

Example Code:
# Step 1: Create an empty list
numbers = []

# Step 2: Collect 5 numbers from the user
print("Enter 5 numbers:")
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Step 3: Calculate the sum of the numbers
total = sum(numbers)

# Step 4: Calculate the average of the numbers
average = total / len(numbers)

# Step 5: Print the results
print("Your list of numbers is:", numbers)
print("Sum of numbers:", total)
print("Average of numbers:", average)

Expected Output:
If the user enters: 10, 20, 30, 40, 50
Enter 5 numbers:
Enter number 1: 10
Enter number 2: 20
Enter number 3: 30
Enter number 4: 40
Enter number 5: 50
Your list of numbers is: [10, 20, 30, 40, 50]
Sum of numbers: 150
Average of numbers: 30.0

This task introduces:
Collecting user input into a list.
Using sum() to calculate the total.
Performing simple arithmetic with lists.
Introducing len() to determine the number of items in a list.
