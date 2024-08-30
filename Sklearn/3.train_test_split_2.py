
from sklearn import datasets
from sklearn.model_selection import train_test_split


iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y,train_size = .8)

print(X,y,sep="\n",end="\n\n")
print("X_train: ",X_train,end="\n\n")
print("X_test: ",X_test,end="\n\n")
print("y_train: ",y_train,end="\n\n")
print("y_test: ",y_test,end="\n\n")



