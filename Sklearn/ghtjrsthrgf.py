from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn import linear_model
import matplotlib.pyplot as plt

import numpy as np



X = np.array([[x,x] for x in range(101)])
y = np.array([y*2 for y in range(101)])



X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

plt.scatter(X_train.T[0],y_train)
plt.show()


l_reg = linear_model.LinearRegression()
model = l_reg.fit(X_train,y_train)


predictions = model.predict(X_test)
accuracy = accuracy_score(y_test,predictions)

print("y_test: ", y_test)
print("Predictions: ", predictions)
print("Accuracy: ",accuracy)







