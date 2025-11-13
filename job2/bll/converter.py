import json
import os
from typing import List, Dict

from fastavro import writer, parse_schema

from job2.dal.storage import clean_directory, list_json_files


SALES_SCHEMA: Dict = {
    "type": "record",
    "name": "Sale",
    "fields": [
        {"name": "client", "type": "string"},
        {"name": "purchase_date", "type": "string"},
        {"name": "product", "type": "string"},
        {"name": "price", "type": "int"},
    ],
}

PARSED_SCHEMA = parse_schema(SALES_SCHEMA)


def convert_json_to_avro(raw_dir: str, stg_dir: str) -> None:
    """Convert each JSON -> separate AVRO file."""
    clean_directory(stg_dir)

    json_files: List[str] = list_json_files(raw_dir)

    for json_file in json_files:
        input_path = os.path.join(raw_dir, json_file)
        output_filename = json_file.replace(".json", ".avro")
        output_path = os.path.join(stg_dir, output_filename)

        with open(input_path, "r", encoding="utf-8") as f:
            records: List[Dict] = json.load(f)

        with open(output_path, "wb") as out:
            writer(out, PARSED_SCHEMA, records)

        print(f"Created AVRO: {output_path}")
