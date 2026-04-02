import json
import os

MEMORY_FILE = "memory/data.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_memory(data):
    os.makedirs("memory", exist_ok=True)
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


def compute_diff(old, new):
    changes = {}

    for comp in new:
        changes[comp] = {}

        if comp not in old:
            changes[comp] = "NEW COMPETITOR"
            continue

        for key in new[comp]:
            if new[comp][key] != old.get(comp, {}).get(key):
                changes[comp][key] = {
                    "old": old.get(comp, {}).get(key),
                    "new": new[comp][key]
                }

    return changes