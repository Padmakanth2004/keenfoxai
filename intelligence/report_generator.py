import json

def save_report(data):
    with open("output/report.json", "w") as f:
        json.dump(data, f, indent=4)