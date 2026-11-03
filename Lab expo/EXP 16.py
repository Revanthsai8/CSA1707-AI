# Feed Forward Neural Network

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create neural network
model = MLPClassifier(
    hidden_layer_sizes=(10,),
    max_iter=1000,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Predict output
y_pred = model.predict(X_test)

# Display results
print("Predicted Values:", y_pred)
print("Actual Values:", y_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy * 100, "%")

# Predict new sample
sample = [[5.1, 3.5, 1.4, 0.2]]
result = model.predict(sample)

print("New Sample Prediction:", iris.target_names[result[0]])
