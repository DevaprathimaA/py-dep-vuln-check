import json

def get_dependencies():
    deps = []
    try:
        with open("package-lock.json") as f:
            data = json.load(f)
            for name, info in data.get("dependencies", {}).items():
                version = info.get("version", "")
                deps.append({"ecosystem": "npm", "name": name, "version": version})
    except FileNotFoundError:
        pass
    return deps
