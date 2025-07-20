from icrawler.builtin import GoogleImageCrawler
import os

# Define keywords and folder mapping
categories = {
    "Promotion": [
        "sale banner", "discount offer", "limited time offer", "shopping deal banner"
    ],
    "Non-Promotion": [
        "website layout", "product page screenshot", "ecommerce homepage", "product only image"
    ]
}

base_dirs = {
    "train": "data/images/train/",
    "val": "data/images/val/"
}

def download_images():
    for category, keywords in categories.items():
        for split in base_dirs:
            output_dir = os.path.join(base_dirs[split], category)
            os.makedirs(output_dir, exist_ok=True)

            for keyword in keywords:
                print(f"Downloading {split}/{category} for keyword: {keyword}")
                crawler = GoogleImageCrawler(storage={'root_dir': output_dir})
                crawler.crawl(keyword=keyword, max_num=15 if split == 'train' else 5)

if __name__ == "__main__":
    download_images()
