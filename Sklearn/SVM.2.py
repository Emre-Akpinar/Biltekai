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

fX_train = [(x[0], x[1], x[2], x[0]**2, x[1]**2, x[2]**2) for x in X_train]
fX_test = [(x[0], x[1], x[2], x[0]**2, x[1]**2, x[2]**2) for x in X_test]

#Training the model
model.fit(fX_train, y_train)

predictions = model.predict(fX_test)
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

print("\n\n\n")

plt.scatter(X_train.T[0], y_train)
plt.show()



