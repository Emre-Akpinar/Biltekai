from sklearn.model_selection import train_test_split
from sklearn import datasets, metrics
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
import pandas as pd


bc = datasets.load_breast_cancer()
X, y = scale(bc.data), bc.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2)

# See what scaling does
"""X = bc.data
plt.scatter(X.T[0],y)
plt.title("Without scaling")
plt.show()
X = scale(bc.data)
plt.scatter(X.T[0],y)
plt.title("With scaling")
plt.show()"""


#Model

KM = KMeans(n_clusters = 2, random_state=0)

KM.fit(X_train)

labels = KM.labels_
predictions = KM.predict(X_test)
accuracy = metrics.accuracy_score(y_test, predictions)
if(accuracy < .3):                                       # The reason I'm doing that is bc since the model labeling the outcome by itself it could label the 0's as 1's and same otherwise.
    accuracy = 1-accuracy                                # if that happens the accuracy would be below 0.1 or so. This loc prevents that from happening.
print(pd.crosstab(y_train,labels))

print("Labels: ",labels)
print("Actual: ",y_test)
print("Predictions: ",predictions)
print("Accuracy: ",accuracy)
















