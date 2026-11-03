# Decision Tree Algorithm

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Decision Tree model
model = DecisionTreeClassifier(criterion='entropy')

# Train the model
model.fit(X_train, y_train)

# Predict output
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Predicted Values:", y_pred)
print("Actual Values:", y_test)
print("Accuracy:", accuracy * 100, "%")

# Predict a new sample
sample = [[5.1, 3.5, 1.4, 0.2]]
result = model.predict(sample)

print("New Sample Prediction:", iris.target_names[result[0]])
