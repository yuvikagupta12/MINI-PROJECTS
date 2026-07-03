import time
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define base URL format for pagination
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"


def get_rating_number(rating_class):
    """Converts textual star rating classes to integer values using NumPy."""
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }

    # Extract the word matching the text map (e.g., from ['star-rating', 'Three'])
    for cls in rating_class:
        if cls in rating_map:
            return rating_map[cls]

    return np.nan


def scrape_books(max_pages=50):
    """Loops through the sandbox pages to extract titles, prices, and ratings."""
    all_books = []

    print(f"Starting data collection for up to {max_pages} pages...")

    for page in range(1, max_pages + 1):
        url = BASE_URL.format(page)
        response = requests.get(url)

        # Break the loop if a page does not exist (e.g., out of bounds)
        if response.status_code != 200:
            print(f"Reached end of pages or error at page {page}.")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        # Locate all individual book containers
        book_pods = soup.find_all("article", class_="product_pod")

        for pod in book_pods:
            # 1. Title (Extract from the 'title' attribute to get the un-truncated text)
            title = pod.h3.a["title"]

            # 2. Price (Strip the currency symbol '£')
            price_text = pod.find("p", class_="price_color").text
            price_cleaned = float(price_text.replace("£", "").replace("Â", ""))

            # 3. Rating (Extract from the class names of the rating tag)
            rating_element = pod.find("p", class_="star-rating")
            rating_classes = rating_element.get("class", [])
            rating_value = get_rating_number(rating_classes)

            # Keep records organized
            all_books.append(
                {
                    "Title": title,
                    "Price (£)": price_cleaned,
                    "Star Rating": rating_value,
                }
            )

        print(f"Successfully scraped page {page}/{max_pages}")
        time.sleep(0.5)  # Courteous delay between requests

    return all_books


if __name__ == "__main__":
    # Execute the scraper
    scraped_data = scrape_books(max_pages=50)

    # Load data into a Pandas DataFrame
    df = pd.DataFrame(scraped_data)

    # Optional: Fill missing ratings with a default numpy placeholder
    df["Star Rating"] = df["Star Rating"].fillna(np.nan)

    # Save to a structured CSV file without indices
    output_filename = "books_scraped_dataset.csv"
    df.to_csv(output_filename, index=False)

    print(f"\nScraping complete! {len(df)} books successfully saved to:")
    print(f"👉 {output_filename}")