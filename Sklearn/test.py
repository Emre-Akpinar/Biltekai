from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from seaborn import pairplot
import pandas as pd
import numpy as np



X = [[6, 84, 10],
     [5.5, 57, 8],
     [4.11,48,5],
     [6.2,88,11],
     [5.2,55,6],
     [5.76,74,9],
     [5.92,71,10],
     [5,52,7]]
X = np.array(X)

y = [1,0,0,1,0,1,1,0]
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X,y,train_size = .8)

df = pd.DataFrame(X)
pairplot(df)
plt.show()

from sklearn.metrics import accuracy_score

# KNN
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 3, weights = "uniform")
knn.fit(X_train,y_train)
y_pred_knn = knn.predict(X_test)
print("KNN accuracy: ", accuracy_score(y_test,y_pred_knn))


# SVM
from sklearn import svm
svm = svm.SVC()
svm.fit(X_train,y_train)
y_pred_svm = svm.predict(X_test)
print("SVM accuracy: ", accuracy_score(y_test,y_pred_svm))


# Kmeans clustering
from sklearn.cluster import KMeans
KM = KMeans(n_clusters = 2)
KM.fit(X)
labels = KM.labels_
print("KMeans clustering accuracy: ",accuracy_score(y,labels))


# Linear Regression
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X_train,y_train)
y_pred_lin = lin_reg.predict(X_test)
print("Linear Regression accuracy: ",lin_reg.score(X,y))



# Logistic Regression
from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(X_train,y_train)
y_pred_log = log_reg.predict(X_test)

print("Logistic Regression accuracy/R^2 : ",accuracy_score(y_test,y_pred_log))











