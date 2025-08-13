import os

SUPPORTED_FILES = {
    "python": ["requirements.txt", "Pipfile", "pyproject.toml"],
    "node": ["package.json", "yarn.lock", "pnpm-lock.yaml"],
    "java": ["pom.xml", "build.gradle", "build.gradle.kts"],
    # Add more ecosystems as needed
}

def discover_dependency_files(root_dir="."):
    """
    Recursively scans the given directory for known dependency files.
    
    Args:
        root_dir (str): Path to the user's project directory.
    
    Returns:
        List[Dict]: A list of dictionaries with language and file_path keys.
    """
    found_files = []

    # Normalize path
    root_dir = os.path.abspath(root_dir)

    for dirpath, _, filenames in os.walk(root_dir):
        for lang, patterns in SUPPORTED_FILES.items():
            for pattern in patterns:
                if pattern in filenames:
                    found_files.append({
                        "language": lang,
                        "file_path": os.path.join(dirpath, pattern)
                    })

    return found_files
