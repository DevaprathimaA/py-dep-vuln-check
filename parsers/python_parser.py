def get_dependencies():
    deps = []
    try:
        with open("requirements.txt") as f:
            for line in f:
                if "==" in line:
                    name, version = line.strip().split("==")
                    deps.append({"ecosystem": "PyPI", "name": name, "version": version})
    except FileNotFoundError:
        pass
    return deps
