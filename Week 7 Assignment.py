# Author: Dalton Cone 
# Purpose: Write a class named Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.
# Name: Week7Assignment.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# declaring the np array to train our model
# here x is months and y is stock price each month. All in order.
x = np.array([1,2,3,4,5,6,7,8,9,10,11]).reshape((-1, 1))
y = np.array([10.25,10.45,10.87,10.75,11.2,12.01,12.25, 12.95,12.80,13.05,14.2])

# Create an instance of the class LinearRegression.
model = LinearRegression()

# .fit() fits the model
model.fit(x, y)

rSquare = model.score(x, y)

# Finally we will make predictions.
y_predict = model.predict(x)
print(f"Coefficient of determination is : {rSquare}")

# Lets make prediction for 12th month using simple maths of straight line geometry.
print(f"Stocks price in 12th month is predicted to be : {model.intercept_ + model.coef_ * 12}")

# Finally we will plot our graph.
plt.scatter(x,y,color='#003F72')
plt.plot(x,y_predict)
plt.xlabel("Month")
plt.ylabel("Stock Price")
plt.show()