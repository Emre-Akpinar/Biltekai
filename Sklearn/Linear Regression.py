from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target

print(X)
print()
print(y)
print("----------------------------------------------------------------------")

# Algorithm
l_reg = linear_model.LinearRegression()

ax = plt.axes(projection="3d")
ax.scatter(X.T[2],y)  # plt.scatter(X[:,0, y)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=.2)

# create the model and train
model = l_reg.fit(X_train,y_train)

predictions = model.predict(X_test)
print("y_test: ", y_test)
print("Predictions: ",predictions)
print("R^2 value: ", l_reg.score(X,y))
print("coedd: ",l_reg.coef_)
print("intercept: ", l_reg.intercept_)
