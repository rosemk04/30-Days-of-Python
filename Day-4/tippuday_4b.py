''' AUTHOR : S TIPPU SAHIB
DESCRIPTION: Write a Program to Swap the Values of Two Variables

'''
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")

print("\nBefore swapping:")
print(f"a = {a}, b = {b}")
a, b = b, a

print("\nAfter swapping:")
print(f"a = {a}, b = {b}")
