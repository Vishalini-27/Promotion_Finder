import json
import pandas as pd
import os

PROMO_KEYWORDS = ['discount', 'sale', 'offer', 'deal', 'save', 'limited', 'off', '%']

def is_promotion(text):
    return any(keyword.lower() in text.lower() for keyword in PROMO_KEYWORDS)

def label_data():
    input_path = os.path.join('data', 'raw_scraped.json')
    output_path = os.path.join('data', 'labeled_data.csv')

    if not os.path.exists(input_path):
        print(f"Input file not found: {input_path}")
        return

    # Load raw scraped data
    with open(input_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    labeled = []
    promo_count = 0
    nonpromo_count = 0

    for entry in raw_data:
        text = entry.get('text', '').strip()
        source = entry.get('website', 'Unknown')

        if not text:
            continue

        label = 'Promotion' if is_promotion(text) else 'Non-Promotion'
        if label == 'Promotion':
            promo_count += 1
        else:
            nonpromo_count += 1

        labeled.append({'text': text, 'label': label, 'source': source})

    # Add synthetic non-promotional examples if needed
    if promo_count > 0 and nonpromo_count == 0:
        print("Only promotion texts found. Adding synthetic non-promotion examples.")
        synthetic_texts = [
            "This is a product description.",
            "Customer reviews are available below.",
            "Free shipping on all orders.",
            "Check product specifications here.",
            "Items in your cart are saved.",
            "This item is currently out of stock.",
            "Please read the return policy.",
            "Add to wishlist for later."
        ]
        for text in synthetic_texts:
            labeled.append({'text': text, 'label': 'Non-Promotion', 'source': 'synthetic'})
            nonpromo_count += 1

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save to CSV
    df = pd.DataFrame(labeled)
    df.to_csv(output_path, index=False, encoding='utf-8')

    print(f"Labeling complete: {promo_count} Promotion, {nonpromo_count} Non-Promotion")
    print(f"Labeled data saved to {output_path}")

if __name__ == '__main__':
    label_data()
