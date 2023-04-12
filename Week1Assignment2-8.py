# Author: Dalton Cone 1/13/2023
# Purpose: To write a program that calculates the total amount of a meal purchased at a restaurant.
# Name Week1Assignment2-8.py

#Constants
TIP = 0.18
SALES_TAX = 0.07

#Inputs
totalFoodCost = float(input("Enter the total charge for food. "))

#Calculations
tipAmount = totalFoodCost * TIP 
salesTaxAmount = totalFoodCost * SALES_TAX
totalCost = tipAmount + salesTaxAmount + totalFoodCost

#Outputs
print("The tip amount is ", '%.2f' % tipAmount)
print("The sales tax is ", '%.2f' % salesTaxAmount)
print("The total cost is ", '%.2f' % totalCost)

