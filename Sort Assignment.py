"""
Name:       sortAssignment.py
Purpose:    Print 3 numbers in ascending order.
Author:     Daltonb Cone
"""

#Inputs
number1 = int(input("Enter a number:"))
number2 = int(input("Enter another number:"))
number3 = int(input("Enter another number:"))

#Calculation
if number1 < number2 < number3:
    print("Here are your numbers in ascending order",number1,number2,number3)
elif number1 < number3 < number2:
    print("Here are your numbers in ascending order",number1,number3,number2)
elif number2 < number1 < number3:
     print("Here are your numbers in ascending order",number2,number1,number3)
elif number2 < number3 < number1:
     print("Here are your numbers in ascending order",number2,number3,number1)
elif number3 < number1 < number2:
     print("Here are your numbers in ascending order",number3,number1,number2)
else:
     print("Here are your numbers in ascending order",number3,number2,number1)
        
        
