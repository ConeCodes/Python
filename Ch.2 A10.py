"""
Name:    ch2Assignment10.py
Purpose: To calculate and employees wage.
Author:  Dalton Cone
"""

# Inputs
hourlyWage = float(input("Enter your hourly wage:"))
regularHours = int(input("Enter your total regular hours:"))
overtimeHours = int(input("Enter your total overtime hours:"))

# Calculations
overTime_pay = overtimeHours * (1.5 * hourlyWage)
totalPay = (hourlyWage * regularHours) + overTime_pay

# Results
print("You made $" , + totalPay, "this week.")
