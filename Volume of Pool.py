"""

Name:      swimmingPool.py
Purpose:   To calculate and display the amount in cubic feet of water in a swimming pool.
Author:    Dalton Cone 8/26/2020

"""

#Inputs
depthShallow = float(input("Enter the depth for the shallow end:"))
depthDeep = float(input("Enter the depth for the deep end:"))
length = float(input("Enter the length:"))
width = float(input("Enter the width:"))

#Calculate
volumeRectangle = depthShallow * length * width
volumeTriangle = .5 * (depthDeep - depthShallow) * length * width
Total = volumeRectangle + volumeTriangle

#Display Results
print("The total amount of water the pool can hold is", Total, " cubic feet of water.")
