# Support Vector Machine
# A clear and fast explanation: https://www.youtube.com/watch?v=_YPScrckx28&pp=ygUDU1ZN

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics




iris = datasets.load_iris()

X = iris.data
y = iris.target

classes = ["iris Setosa", "iris Versicolor", "iris Virginica"]

X_train, X_test, y_train, y_test = train_test_split(X,y,train_size = .8)


#Creating the model
model = svm.SVC()

#Training the model
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = metrics.accuracy_score(y_test, predictions)

y_test_names = []
for i in y_test:
    y_test_names.append(classes[i])

predictions_names = []
for j in predictions:
    predictions_names.append(classes[j])



print("y_test: ", y_test)
print("y_test: ", y_test_names)
print("Predictions: ", predictions)
print("Predictions: ", predictions_names)
print("Accuracy: ", accuracy)




