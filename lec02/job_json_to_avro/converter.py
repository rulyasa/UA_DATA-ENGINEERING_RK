 # placeholder for converter logic
import os
import json
from fastavro import writer, parse_schema


def infer_type(value):
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return "boolean"
    elif isinstance(value, int):
        return "int"
    elif isinstance(value, float):
        return "float"
    else:
        return "string"


def build_avro_schema(records):
    sample_record = records[0]
    fields = []
    for k, v in sample_record.items():
        field_type = infer_type(v)
        fields.append({"name": k, "type": ["null", field_type]})
    schema = {
        "name": "SalesRecord",
        "type": "record",
        "fields": fields
    }
    return parse_schema(schema)


def convert_json_to_avro(raw_dir: str, stg_dir: str):
    os.makedirs(stg_dir, exist_ok=True)

    json_files = [f for f in os.listdir(raw_dir) if f.endswith(".json")]
    if not json_files:
        raise FileNotFoundError("Not found JSON files in raw_dir")

    input_path = os.path.join(raw_dir, json_files[0])
    output_path = os.path.join(stg_dir, json_files[0].replace(".json", ".avro"))

    with open(input_path, "r", encoding="utf-8") as f:
        records = json.load(f)

    if isinstance(records, dict):
        records = [records]

    schema = build_avro_schema(records)

    with open(output_path, "wb") as out:
        writer(out, schema, records)

    print(f"Data was converted to Avro: {output_path}")
