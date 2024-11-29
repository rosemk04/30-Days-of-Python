'''AUTHOE:SEBIN PRINCE
DESCRIPTION: Find the Sum and Average of Numbers in a List Instructions: 1.Ask the user to input 5 numbers, one at a time, and store them in a list. 2.Calculate and print the sum of all numbers in the list. 3.Calculate and print the average of the numbers.
'''
numbers=[]
for i in range(5):
    num=float(input("Enter numbers:"))
    i+1
    numbers.append(num)
total_sum=sum(numbers)
print("Total sum is:",total_sum)
average=total_sum/len(numbers)
print("Average is:",average)
