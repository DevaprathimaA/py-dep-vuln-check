import json

def load_suppressions():
    try:
        with open("suppress.json") as f:
            return json.load(f).get("suppress", [])
    except FileNotFoundError:
        return []
