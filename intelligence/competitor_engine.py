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

# 🔹 Clean raw data
def clean_data(data):
    if not data:
        return []

    cleaned = []
    for d in data:
        if d and isinstance(d, str):
            text = d.strip()
            if text:
                cleaned.append(text)

    return cleaned


# 🔹 Remove duplicates + noise
def preprocess_data(data, limit=100):
    data = list(set(data))

    cleaned = []
    for d in data:
        text = str(d).strip()
        if text and len(text) > 3:
            cleaned.append(text)

    return cleaned[:limit]


# 🔹 Validate extracted signals
def validate_analysis(analysis):
    if not isinstance(analysis, dict):
        return {"error": "Invalid analysis format"}

    cleaned = {
        k: v for k, v in analysis.items()
        if v not in [None, "", [], {}, "N/A"]
    }

    if not cleaned:
        return {"error": "Empty analysis"}

    return cleaned


def run_engine():
    results = {}

    for name, url in competitors.items():
        try:
            # 🔹 Step 1: Collect data
            web_data = clean_data(scrape_website(url))
            reddit_data = clean_data(fetch_reddit_data())
            reviews_data = clean_data(load_reviews())

            combined = web_data + reddit_data + reviews_data

            # ✅ Guardrail 1: No data
            if not combined:
                print(f"⚠️ No data for {name}")
                results[name] = {"error": "No data collected"}
                continue

            # 🔹 Step 2: Preprocess (VERY IMPORTANT)
            combined = preprocess_data(combined)

            # ✅ Guardrail 2: Still empty after cleaning
            if not combined:
            # fallback to raw data (important)
                combined = web_data + reddit_data + reviews_data
                if not combined:
                    results[name] = {"error": "No data collected"}
                    continue

            # 🔹 Step 3: Extract signals
            analysis = extract_signals(combined)

            # 🔹 Step 4: Validate
            validated = validate_analysis(analysis)

            results[name] = validated

        except Exception as e:
            print(f"❌ Error processing {name}: {e}")
            results[name] = {"error": str(e)}

    return results