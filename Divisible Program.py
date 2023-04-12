"""
Name:        divisibleProgram.py
Purpose:     Write a program that prompts the user to enter an integer and checks whether the number is divisible by both 5 and 6, divisible by 5 or 6, or just one of them (but not both).
Author:      Dalton Cone
"""

integer=int(input('Enter an integer:'))
if integer%5==0 and integer%6==0:
    print('Is',integer,'divisible by 5 and 6? True')
else:
    print('Is',integer,'divisible by 5 and 6? False')
if integer%5==0 or integer%6==0:
    print('Is',integer,'divisible by 5 or 6? True')
else:
    print('Is',integer,'divisible by 5 or 6? False')
if ((integer%5==0 and integer%6!=0) or (integer%5!=0 and integer%6==0)):
    print('Is',integer,'divisible by 5 or 6, but not both? True')
else:
    print('Is',integer,'divisible by 5 or 6, but not both? False')

            
            
