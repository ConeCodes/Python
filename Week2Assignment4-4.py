# Author: Dalton Cone 
# Purpose: Write a program that asks the user for the speed of a vehicle (in miles per hour) and the number of hours it has traveled. 
# It should then use a loop to display the distance the vehicle has traveled for each hour of that time period.
# Name Week2Assignment4-4.py

#Inputs
speed = int(input("\nWhat is the speed of the vehicle in mph? "))
hours = int(input("How many hours has the vehicle traveled? "))

#Calculations and Output
print("\nHours\tDistance Traveled")

for time in range (1, hours+1):     # For loop to calculate and display the hour and distance traveled.
    distance = speed * time
    print(time, "\t", distance)



