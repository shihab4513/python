import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
# This line reads a CSV file named ‘dataset.csv’ and stores the data in a DataFrame df.
df = pd.read_csv('dataset.csv')

# Drop the 'Roll' column as it is not needed for the prediction
df = df.drop(['Roll'], axis=1)


# Normalize the features
# These lines create an instance of MinMaxScaler and use it to normalize the features in df.
scaler = MinMaxScaler()
df[df.columns[:-1]] = scaler.fit_transform(df[df.columns[:-1]])

# Split the dataset into features (X) and target (y)
# These lines split the DataFrame df into features X and target y.
X = df[df.columns[:-1]]
y = df['Section']

# Split the dataset into training, validation, and testing sets
# These lines split the dataset into training, validation, and testing sets.
X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.1111, random_state=42)


# Initialize variables to store the best K value and its accuracy
best_k = 0
best_accuracy = 0

# Iterate over the possible K values
# These lines iterate over possible K values (1, 3, 5, 7), fit a KNN model for each K value, predict the validation data, calculate the accuracy of the model, and update the best K value and its accuracy if the current model’s accuracy is better than the best accuracy found so far.
for k in [1, 3, 5, 7]:
    # Initialize the KNN classifier with the current K value
    knn = KNeighborsClassifier(n_neighbors=k)


    # Fit the model with the training data
    knn.fit(X_train, y_train)

    # Predict the validation data
    y_val_pred = knn.predict(X_val)

    # Calculate the accuracy of the current model
    accuracy = accuracy_score(y_val, y_val_pred)

    # If the current model's accuracy is better than the best accuracy found so far, update the best K value and its accuracy
    if accuracy > best_accuracy:
        best_k = k
        best_accuracy = accuracy

# These lines initialize a KNN classifier with the best K value, fit the model with the combined training and validation data, predict the testing data, and calculate the accuracy of the final model.
# Initialize the KNN classifier with the best K value
knn = KNeighborsClassifier(n_neighbors=best_k)

# Fit the model with the training and validation data
knn.fit(X_train_val, y_train_val)

# Predict the testing data
y_test_pred = knn.predict(X_test)

# Calculate the accuracy of the final model
accuracy = accuracy_score(y_test, y_test_pred)

# This line prints the best K value and the accuracy of the final model on the testing set.
# Print the best K value and the accuracy of the final model
# print(f"The best K value is {best_k} with an accuracy of {accuracy} on the testing set.")
print(f"The best K value is {best_k} with validation accuracy of {best_accuracy}.")
print(f"The test accuracy is {accuracy}.")
