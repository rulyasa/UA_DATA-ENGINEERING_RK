 # placeholder for fetcher logic
import os
import json
import shutil
import requests
from datetime import datetime


def fetch_data(api_url: str):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()


def save_raw_data(data, raw_dir: str):
    if os.path.exists(raw_dir):
        shutil.rmtree(raw_dir)
    os.makedirs(raw_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(raw_dir, f"data_{timestamp}.json")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Data was saved to: {output_file}")
    return output_file