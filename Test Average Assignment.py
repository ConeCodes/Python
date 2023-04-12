"""
Name:        testAverage.py
Purpose:     Create a Python program for Mrs. Smart that will allow her to calculate student test averages regardless of how many tests will be averaged.
Author:      Dalton Cone
"""
total = 0
n = 0
total = 0
more = "y"

while more == "y":
    grade = float(input("Enter a test grade:"))
    n += 1
    total += grade
    more = input("Are there anymore test grades to enter, y or n ?")
print("The average is %1.1f" % (total/n))
while more == "n":
    student=(input("Are there any more students, y or n ?"))
    if student == "y":
        grade = float(input("Enter a test grade:"))
        n += 1
        total += grade
        more = input("Are there anymore test grades to enter, y or n ?")
    else:
            print("I'm done")
    
    
   


