'''Author:Riya Ann Mathew
Description:program to swap the values of two variables'''
x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
print(f"before swapping:x={x},y={y}")
temp=x
x=y
y=temp
print(f"after swapping :x={x},y={y}")