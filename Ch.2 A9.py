"""
Name:         ch2Assignment9.py
Purpose:      Takes the number of input for kilometers and prints the corresponding number of nautical miles. 
Author:       Dalton Cone
Useful Info:  1 Kilo = 0.5399568035 Nautical Mile
"""

# Input
kilometer = float(input("Enter the number of kilometers:"))

# Calculate
nauticalMile = kilometer * 0.5399568035

# Result
print(kilometer, "is", nauticalMile, "nauticle mile")
