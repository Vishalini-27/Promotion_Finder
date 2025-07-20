import os
import json
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Resolve base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

# Load scraped raw text data
raw_data_path = os.path.join(PROJECT_ROOT, 'data', 'raw_scraped.json')
with open(raw_data_path, 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

texts = [entry.get('text', '') for entry in raw_data if entry.get('text')]

# Load model and vectorizer from predictions/
model_path = os.path.join(BASE_DIR, 'text_model.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'vectorizer.pkl')

# Load trained model and vectorizer
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Transform input texts and predict
X = vectorizer.transform(texts)
predictions = model.predict(X)

# Display and save predictions
for text, label in zip(texts, predictions):
    print(f"\nText: {text}\n→ Prediction: {label}")

# Save to CSV
df = pd.DataFrame({'Text': texts, 'Predicted_Label': predictions})
output_csv = os.path.join(BASE_DIR, 'predicted_output.csv')
df.to_csv(output_csv, index=False, encoding='utf-8')
print("\nAll predictions saved to predictions/predicted_output.csv")
