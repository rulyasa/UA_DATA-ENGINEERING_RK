import os
import requests
from typing import List, Dict, Optional

from job1.dal.storage import clean_directory, save_json_page

API_URL = "https://fake-api-vycpfa6oca-uc.a.run.app/sales"


def fetch_sales_page(date: str, page: int) -> Optional[List[Dict]]:
    """Fetch single page of sales. Returns list or None if page not found."""
    headers = {"Authorization": os.environ["AUTH_TOKEN"]}
    params = {"date": date, "page": page}

    response = requests.get(API_URL, headers=headers, params=params)

    if response.status_code == 404:
        return None

    if response.status_code != 200:
        raise RuntimeError(
            f"API error {response.status_code}: {response.text}"
        )

    return response.json()


def save_sales_to_local_disk(date: str, raw_dir: str) -> None:
    """Download all pages from API and store them into raw_dir."""
    clean_directory(raw_dir)

    page: int = 1
    total_records: int = 0

    while True:
        data = fetch_sales_page(date, page)

        if data is None or not data:
            break

        save_json_page(directory=raw_dir, date=date, page=page, content=data)
        total_records += len(data)
        page += 1

    print(f"Saved {total_records} total records.")
