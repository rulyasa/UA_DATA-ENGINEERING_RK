import json
import os
import shutil
from typing import List


def clean_directory(path: str) -> None:
    """Remove directory and recreate it empty."""
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)


def save_json_page(directory: str, date: str, page: int,
                   content: list) -> None:
    """Save one API page into JSON file."""
    filename = f"sales_{date}_{page}.json"
    full_path = os.path.join(directory, filename)

    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(content, f, indent=2)

    print(f"Saved file: {full_path}")


def list_json_files(path: str) -> List[str]:
    """Return list of JSON files in the directory."""
    if not os.path.exists(path):
        return []
    return [f for f in os.listdir(path) if f.endswith(".json")]
