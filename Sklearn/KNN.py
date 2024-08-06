# K nearest neighbor classifier

import numpy as np
import pandas as pd
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# ----------------

data = pd.read_csv("car.data")

X = data[["buying","maint","doors","persons","lug_boot","safety"]].values
y = data[["acceptibility"]]
print(X, y.head(), sep="\n\n", end="\n\n")

# Converting the X data using LabelEncoder
Le = LabelEncoder()

for i in range(len(X[0])):
    X[:,i] = Le.fit_transform(X[:,i])

print(X)

# Converting y data using maping
label_maping = {
    "unacc": 0,
    "acc": 1,
    "good":2,
    "vgood":3
}

y["acceptibility"] = y["acceptibility"].map(label_maping)
y = np.array(y)
print(y)

# ----------------


# Creating the model

# knn object                       #also known as 'k'
knn = neighbors.KNeighborsClassifier(n_neighbors=25, weights='uniform')

# creating the training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y,train_size=.8)

# training the model with training sets
knn.fit(X_train, y_train)

# predicting the label using test features
predictions = knn.predict(X_test)

# Checking how accurate the prediction by comparing the predictions and test labels
accuracy = metrics.accuracy_score(y_test, predictions)
print()
print("test labels: ",y_test.reshape(predictions.shape))
print("Predictions: ",predictions)
print("Accuracy: ",accuracy)
print("------------------------------------------------------------------------")
print("Actual value: ",y_test[255])
print("Predicted value: ",knn.predict(X_test)[255])
