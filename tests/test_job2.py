import os
import json
from fastavro import reader

from job2.bll.converter import convert_json_to_avro


def test_job2_converts_json_to_avro(tmp_path):
    """Job2 should create separate AVRO for each JSON"""

    raw_dir = tmp_path / "raw" / "sales" / "2022-08-09"
    stg_dir = tmp_path / "stg" / "sales" / "2022-08-09"

    os.makedirs(raw_dir, exist_ok=True)

    # Creating 4 JSON-files like it was created by job1
    for i in range(1, 5):
        payload = [
            {
                "client": f"Client {i}",
                "purchase_date": "2022-08-09",
                "product": "TV",
                "price": i * 100,
            }
        ]
        with open(raw_dir / f"sales_2022-08-09_{i}.json", "w",
                  encoding="utf-8") as f:
            json.dump(payload, f, indent=2)

    convert_json_to_avro(
        raw_dir=str(raw_dir),
        stg_dir=str(stg_dir),
    )

    files = sorted(os.listdir(stg_dir))
    assert files == [
        "sales_2022-08-09_1.avro",
        "sales_2022-08-09_2.avro",
        "sales_2022-08-09_3.avro",
        "sales_2022-08-09_4.avro",
    ]

    # Checking content of first avro
    avro_path = stg_dir / "sales_2022-08-09_1.avro"
    with open(avro_path, "rb") as f:
        records = list(reader(f))

    assert len(records) == 1
    assert records[0]["client"] == "Client 1"
    assert records[0]["price"] == 100
