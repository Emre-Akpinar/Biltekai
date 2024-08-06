# This is used to split the sets that we gonna train the model(train set) and test the model(test set)


import pandas as pd
from sklearn.model_selection import train_test_split


# importing data
df = pd.read_csv('headbrain1.csv')

# head of the data
print(df.head())

X= df['Head Size(cm^3)']
y=df['Brain Weight(grams)']

# using the train test split function                       # 1-%25test.set 2-%80train.set  It is suggested to keep our train sets larger than the test sets.
X_train, X_test, y_train, y_test = train_test_split(X,y , random_state=104, test_size=0.25, shuffle=True)
#X_train, X_test, y_train, y_test = train_test_split(X,y , random_state=104, train_size=0.8, shuffle=True)

# printing out train and test sets

print('X_train : ')
print(X_train.head())
print('')
print('X_test : ')
print(X_test.head())
print('')
print('y_train : ')
print(y_train.head())
print('')
print('y_test : ')
print(y_test.head())
