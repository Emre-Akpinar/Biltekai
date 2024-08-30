import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import neighbors, metrics
from sklearn import datasets
from seaborn import pairplot
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

wine = datasets.load_wine()

X = wine.data
y = wine.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2)

#Scaling the data (Before scaling accuracy appexmtly .7, after scaling accuracy apprxmtly .9)
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.fit_transform(X_test)





#Converting data to dataframe
df = pd.DataFrame(X_train, columns = wine.feature_names)
df["Wine Class"] = y_train
df["Wine Class"] = df["Wine Class"].replace(to_replace=[0,1,2], value=["class_0","class_1","class_2"])


#creating plot using seaborn
pairplot(data = df, hue = "Wine Class", palette = "Set2")
plt.show()








# Model

# object
knn = neighbors.KNeighborsClassifier(n_neighbors=7, weights="uniform")

# train
knn.fit(X_train, y_train)

predictions = knn.predict(X_test)
accuracy = metrics.accuracy_score(y_test,predictions)
print("y_test:      ",y_test)
print("Predictions: ",predictions)
print("Accuracy: ",accuracy)
















