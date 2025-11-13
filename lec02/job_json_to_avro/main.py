from converter import convert_json_to_avro


def main():
    raw_dir = "job_fetch_raw/raw_dir"
    stg_dir = "job_json_to_avro/stg_dir"

    print("🚀 Convertation JSON → Avro...")
    convert_json_to_avro(raw_dir, stg_dir)


if __name__ == "__main__":
    main()