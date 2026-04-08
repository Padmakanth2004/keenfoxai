import json
import os

def save_report(data):
    try:
        os.makedirs("output", exist_ok=True)

        with open("output/report.json", "w") as f:
            json.dump(data, f, indent=4)

    except Exception as e:
        print(f"Error saving report: {e}")