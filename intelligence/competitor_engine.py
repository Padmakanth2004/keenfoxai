from ingestion.web_scraper import scrape_website
from ingestion.reddit_scraper import fetch_reddit_data
from ingestion.reviews_loader import load_reviews
from processing.signal_extractor import extract_signals

competitors = {
    "Notion": "https://www.notion.so",
    "Asana": "https://asana.com",
    "ClickUp": "https://clickup.com",
    "Monday": "https://monday.com"
}

def run_engine():
    results = {}

    for name, url in competitors.items():
        web_data = scrape_website(url)
        reddit_data = fetch_reddit_data()
        reviews_data = load_reviews()

        combined = web_data + reddit_data + reviews_data

        analysis = extract_signals(combined)

        # ✅ NEW: Error handling for invalid JSON from LLM
        if isinstance(analysis, dict) and "error" in analysis:
            print(f"⚠️ Parsing failed for {name}")

        results[name] = analysis

    return results