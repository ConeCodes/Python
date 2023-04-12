# Author: Dalton Cone 
# Purpose: Your manager wants you to provide some reports from the sales this month that involves some data manipulation through Python.
# Name: Week6Assignment.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("sampledatafoodsales.xlsx", sheet_name= "FoodSales")


x = list(data['Product'])
y = list(data['UnitPrice'])

plt.plot(x, y, color ='maroon')
plt.show()
   