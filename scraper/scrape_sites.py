import requests
from bs4 import BeautifulSoup
import os
import json

KEYWORDS = ["offer", "discount", "deal", "% off", "sale"]

def extract_promotions(texts):
    return [t for t in texts if any(k.lower() in t.lower() for k in KEYWORDS)]

def scrape_amazon():
    print("[*] Scraping Amazon...")
    url = "https://www.amazon.in/s?k=offers"
    soup = BeautifulSoup(requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text, "html.parser")
    texts = [tag.get_text(strip=True) for tag in soup.find_all("span")]
    return extract_promotions(texts)

def scrape_flipkart():
    print("[*] Scraping Flipkart...")
    url = "https://www.flipkart.com/search?q=offers"
    soup = BeautifulSoup(requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text, "html.parser")
    texts = [tag.get_text(strip=True) for tag in soup.find_all("div")]
    return extract_promotions(texts)

def scrape_walmart():
    print("[*] Scraping Walmart...")
    url = "https://www.walmart.com/search?q=offers"
    soup = BeautifulSoup(requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text, "html.parser")
    texts = [tag.get_text(strip=True) for tag in soup.find_all("span")]
    return extract_promotions(texts)

def scrape():
    all_promos = []
    all_promos += scrape_amazon()
    all_promos += scrape_flipkart()
    all_promos += scrape_walmart()

    final_data = [{"text": promo} for promo in all_promos]
    
    # SAVE PATH - Your full absolute path
    output_path = r"C:\Users\DELL\Downloads\Promotion_Finder_Project\Promotion_Finder_Project\data\raw_scraped.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)

    print(f"[✓] Scraped {len(final_data)} promotional texts from 3 sites.")

if __name__ == "__main__":
    scrape()
