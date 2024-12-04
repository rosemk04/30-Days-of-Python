'''
Author:Parvathy J Nair
Description:Write a Python program that asks the user to enter a password. If the entered password matches a predefined password,
 print "Access granted"; otherwise, print "Access denied."
 '''
predefined_password="secure123"
user_password=input("Enter a password:")
if user_password==predefined_password:
    print("Access Granted")
else:
    print("Access Denied")