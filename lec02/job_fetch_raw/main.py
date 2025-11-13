import json
from fetcher import fetch_data, save_raw_data

CONFIG_PATH = "job_fetch_raw/config.json"


def main():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)

    api_url = config["api_url"]
    raw_dir = config["raw_dir"]

    print("Loading data...")
    data = fetch_data(api_url)

    print("Saving data in raw_dir...")
    save_raw_data(data, raw_dir)


if __name__ == "__main__":
    main()