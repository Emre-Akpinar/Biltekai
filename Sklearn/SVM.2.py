# Support Vector Machine
# A clear and fast explanation: https://www.youtube.com/watch?v=_YPScrckx28&pp=ygUDU1ZN

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
import numpy as np
from sklearn.metrics import confusion_matrix




iris = datasets.load_iris()

X = iris.data
y = iris.target

classes = ["iris Setosa", "iris Versicolor", "iris Virginica"]

X_train, X_test, y_train, y_test = train_test_split(X,y,train_size = .8,random_state = 42)


# Creating the model
model = svm.SVC()

# non_linear transformation(watch this: https://www.youtube.com/watch?v=Q7vT0--5VII  : about svm kernal tricks)
fX_train = [(x[0], x[1], x[2], x[0]**2, x[1]**2, x[2]**2) for x in X_train]
fX_train = np.array(fX_train)
fX_test = [(x[0], x[1], x[2], x[0]**2, x[1]**2, x[2]**2) for x in X_test]
fX_test = np.array(fX_test)
# Using kernel when creating the model can help because it does what i did above without any additional process




# Training the model
model.fit(fX_train, y_train)

predictions = model.predict(fX_test)
accuracy = metrics.accuracy_score(y_test, predictions)

###
y_test_names = []
for i in y_test:
    y_test_names.append(classes[i])

predictions_names = []
for j in predictions:
    predictions_names.append(classes[j])
###


print("y_test: ", y_test)
print("y_test: ", y_test_names)
print("Predictions: ", predictions)
print("Predictions: ", predictions_names)
print("Accuracy: ", accuracy)

conf_mat = confusion_matrix(y_test,predictions)
print("Confusion Matrix: \n",conf_mat)





plt.scatter(X_train.T[0], y_train)
plt.show()


