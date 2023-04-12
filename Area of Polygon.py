"""
Name:     areaOfPolygon.py
Purpose:  To calculate and display the area of a polygon.
Authir:   Dalton Cone 8/26/2020

"""

#Inputs
apothem = float(input("Enter the measure of the apothem:"))
numbersides = int(input("Enter the total number of sides:"))
length = float(input("Enter the length of one of the sides:"))

#Calculate
area = .5 * apothem * numbersides * length

#Display Results
print("The area of the polygon is", area, "units.")  
