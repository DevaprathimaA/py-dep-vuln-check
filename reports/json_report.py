import json

def generate(results, path):
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
