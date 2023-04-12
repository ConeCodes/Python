"""
Name:         ch6Assignment.py
Purpose:      Compute the square root of the number.
Author:       Dalton Cone

"""
import math

#Initialize tolerance
TOLERANCE = 0.000001

def newton(x, estimate):
    """ Returns the square root of x."""
    
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference <= TOLERANCE:
        return estimate
    else:

        return newton(x,estimate)
                          
                           

def main():
    while True:
        x = input("Enter a positive number or enter/return to quit:")
        if x == "":
            break
        x = float(x)
        estimate = 1.0
        print("The program's estimate is", newton(x,estimate))
        print("Python's estimate is ", math.sqrt(x))
main()
