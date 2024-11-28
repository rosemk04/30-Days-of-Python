
Task: Find the Union and Intersection of Two Sets
Objective: Write a Python program that takes two sets, finds their union and intersection, and displays the results.

Instructions:
1.Open your coding environment: Use a code editor, IDE, or Python terminal to write your program.
2.Write the code: Enter the following Python code into your script:

# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Calculate the union of the two sets
union_result = set1.union(set2)

# Calculate the intersection of the two sets
intersection_result = set1.intersection(set2)

# Display the results
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {union_result}")
print(f"Intersection: {intersection_result}")

3.Run the program: Save and execute the code.
4.Test the program:

For the example sets {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}, the output will be:
Set 1: {1, 2, 3, 4, 5}
Set 2: {4, 5, 6, 7, 8}
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}

Explanation:

Sets: A data type in Python used to store unique elements.
set1.union(set2): Combines all elements from both sets, removing duplicates.
set1.intersection(set2): Finds common elements between the two sets.
print(): Displays the sets and results in a readable format.
