import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


ds = pd.read_csv('dataset.csv')


ds = ds.drop(['Roll'], axis=1)


# Normalize the features
# These lines create an instance of MinMaxScaler and use it to normalize the features in df.
scaler = MinMaxScaler()
ds[ds.columns[:-1]] = scaler.fit_transform(ds[ds.columns[:-1]])


X = ds[ds.columns[:-1]]
y = ds['Section']


X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.1111, random_state=42)



best_k = 0
best_accuracy = 0

# Iterate over the possible K values
# These lines iterate over possible K values (1, 3, 5, 7), fit a KNN model for each K value, predict the validation data, calculate the accuracy of the model, and update the best K value and its accuracy if the current model’s accuracy is better than the best accuracy found so far.
for k in [1, 3, 5, 7]:
    # Initialize the KNN classifier with the current K value
    knn = KNeighborsClassifier(n_neighbors=k)


    # Fit the model with the training data
    knn.fit(X_train, y_train)

    # Predict the validation data for y using  x_val
    y_val_pred = knn.predict(X_val)


    accuracy = accuracy_score(y_val, y_val_pred)


    if accuracy > best_accuracy:
        best_k = k
        best_accuracy = accuracy


knn = KNeighborsClassifier(n_neighbors=best_k)

# Fit the model with the training and validation data
knn.fit(X_train_val, y_train_val)

# Predict the testing data
y_test_pred = knn.predict(X_test)

# Calculate the accuracy of the final model
accuracy = accuracy_score(y_test, y_test_pred)


print("The best k value is " + str(best_k) + " with validation accuracy of " + str(best_accuracy))
print("The test accuracy is " + str(accuracy))


