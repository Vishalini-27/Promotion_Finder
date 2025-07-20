import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load labeled data
df = pd.read_csv('data/labeled_data.csv')

# Split data
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Load the same vectorizer and model used during training
vectorizer = joblib.load('predictions/vectorizer.pkl')
model = joblib.load('predictions/text_model.pkl')

# Transform test data using the saved vectorizer
X_test_vec = vectorizer.transform(X_test)

# Predict and evaluate
y_pred = model.predict(X_test_vec)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy Score:", round(accuracy, 4))

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
