# Author: Dalton Cone 
# Purpose: Write a program that displays the number of names that are stored in the file.
# Name Week2Assignment6-4.py

myfile = open('names.txt', 'r')

#Count the lines in the file
totalLines = len(myfile.readlines())
print("\nThere are a total of", totalLines, "names in my file.")

# Close the file.
myfile.close()