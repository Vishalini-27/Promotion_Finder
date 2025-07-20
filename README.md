# Promotion Finder – Final Report

## Overview
This project leverages machine learning to identify **promotional content** on e-commerce websites by analyzing:
- **Textual content** (scraped from site elements).
- **Visual content** (images such as banners) using a CNN model.

---

## Task Breakdown

### Phase 1: Data Collection
- Scraped Amazon, Flipkart, and Walmart using `requests` and `BeautifulSoup`.
- Extracted key elements like homepage headlines, buttons, and promotional banners.

### Phase 2: Data Labeling
- Automatically labeled scraped text as `Promotion` or `Non-Promotion` based on the presence of keywords such as *“sale”*, *“offer”*, *“discount”*, etc.

### Phase 3: Model Development
- **Text Classifier**: Trained a Logistic Regression model using TF-IDF features.
- **Image Classifier**: Trained a CNN model (on synthetic/mock data) to classify promotional vs non-promotional images.

---

## Evaluation Metrics

- **Text Classification Model**:  
  Accuracy: **~96%** (high accuracy, but recall for non-promotional content is low due to class imbalance).

- **Image Classification Model**:  
  Accuracy: **~90%** *(mocked dataset used for demonstration only)*.

---

## Project Structure

```
/scraper        → Scripts for web scraping
/labeling       → Keyword-based text labeling
/text_model     → TF-IDF + Logistic Regression model
/image_model    → CNN training and evaluation
/predictions    → Prediction scripts and outputs
/data           → Contains raw, labeled, and processed datasets
```

---