import os
import json

from job1.bll.sales_api import save_sales_to_local_disk


def test_job1_creates_raw_json_files(tmp_path, mock_sales_api):
    """Job1 should create 4 JSON-files with correct names"""

    raw_dir = tmp_path / "raw" / "sales" / "2022-08-09"

    save_sales_to_local_disk(
        date="2022-08-09",
        raw_dir=str(raw_dir),
    )

    files = sorted(os.listdir(raw_dir))

    assert files == [
        "sales_2022-08-09_1.json",
        "sales_2022-08-09_2.json",
        "sales_2022-08-09_3.json",
        "sales_2022-08-09_4.json",
    ]

    # Check content of first file
    with open(raw_dir / "sales_2022-08-09_1.json", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["client"] == "A"
    assert data[0]["price"] == 100
