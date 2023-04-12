# Author: Dalton Cone 
# Purpose: Write a program that reads a string from the user containing a date in the form mm/dd/yyyy.
# Name: Week3Assignment8-3.py

months = ['January','February','March','April','May','June','July',
'August','September','October','November','December']

#Input
date_input = input('Enter date in the format mm/dd/yyyy: ').split('/')

#Calculate
month = months[int(date_input[0])-1]
day = int(date_input[1])
year = int(date_input[2])

#Output
print('The date is {} {}, {}'.format(month,day,year))

