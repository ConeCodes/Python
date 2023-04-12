"""
Name:      ch4Assignment1.py
Purpose:   To read an unspecified number of integers, determines how many positive values and negative values have been read, and computes the total and average of the input values.
Author:    Dalton Cone
"""

positive=0
negative=0
total=0
average=0.00

while True:
    number= int(input("Enter an integer, the input ends if it is 0:"))
    if number == 0:
        break
    else:
        total = total + number
        if number < 0 :
            negative = negative + 1
        else:
            positive = positive + 1
            
average = float(total/(positive+negative))
print("The number of positives is",positive)
print("The number of negatives is",negative)
print("The total is",total)
print("The average is",average)
