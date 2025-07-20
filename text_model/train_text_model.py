import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

# Load labeled data
df = pd.read_csv('data/labeled_data.csv')

# Prepare features and labels
X = df['text']
y = df['label']

# Convert text to numerical features
vectorizer = TfidfVectorizer()
X_vect = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42, stratify=y)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Ensure predictions folder exists
os.makedirs('predictions', exist_ok=True)

# Save model and vectorizer
joblib.dump(model, 'predictions/text_model.pkl')
joblib.dump(vectorizer, 'predictions/vectorizer.pkl')
print("Model and vectorizer saved to predictions/")
