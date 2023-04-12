"""
Name:         tipProgram.py
Purpose:      Write a function that expects two parameters, one will be the amount of the dinner check ( a float), and the other one will be the percentage of tip expressed as an integer  (i.e. 20 for 20 percent). The user will give as input these two values. The function will return the amount that the tip should be. Display the results.
Author:       Dalton Cone
"""

def tip (x,y):
    return x/y

dinner=float(input('Enter the amount of the dinner check:'))
percentTip=int(input('Enter the percentage of tip as an integer:'))
result= tip(dinner,percentTip)
print('The tip should be $' + '%1.2f' % result)
    
