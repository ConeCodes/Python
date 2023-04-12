# importing libraries  
import numpy as nump  
import matplotlib.pyplot as mtp  
import pandas as pand  
  
#importing datasets  
Data = pand.read_excel('cal_housing.xlsx')  
  
Data.head()

#remove null values
Data = Data.dropna()

#Extracting Independent and dependent Variable  
x_train = Data.drop('Building Value',axis=1)
y_train = Data['Building Value']

#Fitting K-NN classifier to the training set  
from sklearn.neighbors import KNeighborsClassifier  
classifier= KNeighborsClassifier(n_neighbors=3, metric='minkowski', p=2 )  
classifier.fit(x_train, y_train)

# The house estimate the value for has the following properties:

arr = nump.array([120.75, 39.34, 35.5, 260, 120, 540, 12, 1.8]).reshape(1, -1)

#Predicting the test set result  
y_pred= classifier.predict(arr)  

print(y_pred)