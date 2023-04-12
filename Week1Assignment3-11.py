# Author: Dalton Cone 
# Purpose: Write a program that asks the user to enter the number of books that he or she has purchased this month, then displays the number of points awarded.
# Name Week1Assignment3-11.py

#Inputs
numofBooks = int(input("Enter the number of books you purchased this month."))

#Calculation and Output
if numofBooks == 0:
    print("You earned 0 points.")
else:
    if numofBooks == 2:
        print("You earned 5 points!")
    else:
        if numofBooks == 4:
            print("You earned 15 points!")
        else:
            if numofBooks == 6:
                print("You earned 30 points!")
            else:
                if numofBooks >= 8:
                    print("You earned 60 points!")
                else:
                    print("Error. Value must be 0, 2, 4, 6, 8 or higher.")
                    
