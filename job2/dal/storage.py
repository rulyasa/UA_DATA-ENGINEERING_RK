import os
import shutil


def clean_directory(path: str):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)


def list_json_files(path: str):
    if not os.path.exists(path):
        return []

    return [f for f in os.listdir(path) if f.endswith(".json")]
