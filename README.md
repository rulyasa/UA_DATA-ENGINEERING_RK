📦 Data Engineering Homework (lec02)
🧩 Project Overview

Цей проєкт реалізує ETL pipeline:

1. Job1 (API → RAW JSON)

Отримує дані продажів з REST API

Зберігає їх у JSON-файли у форматі

raw/sales/<date>/sales_<date>_<page>.json


Ідемпотентна: перед записом очищає директорію

2. Job2 (RAW JSON → AVRO)

Конвертує всі JSON-файли у AVRO

Зберігає у форматі

stg/sales/<date>/sales_<date>_<page>.avro


3. Юніт-тести (pytest)

Mock API для job1

Перевірка генерації JSON

Перевірка конвертації у AVRO

Використано fastavro

📁 Project Structure
lec02/
│
├── job1/
│   ├── main.py
│   ├── bll/
│   │    └── sales_api.py
│   └── dal/
│        └── storage.py
│
├── job2/
│   ├── main.py
│   ├── bll/
│   │    └── converter.py
│   └── dal/
│        └── storage.py
│
├── tests/
│   ├── test_job1.py
│   ├── test_job2.py
│   └── conftest.py
│
├── pyproject.toml
└── README.md

🚀 Running Job1

Start API extraction job:

python job1/main.py


Send POST request:

curl -X POST http://localhost:8081/ \
  -H "Content-Type: application/json" \
  -d "{ \"date\": \"2022-08-09\", \"raw_dir\": \"./file_storage/raw/sales/2022-08-09\" }"

🔄 Running Job2

Start Avro converter:

python job2/main.py


POST request:

curl -X POST http://localhost:8082/ \
  -H "Content-Type: application/json" \
  -d "{ \"raw_dir\": \"./file_storage/raw/sales/2022-08-09\", \"stg_dir\": \"./file_storage/stg/sales/2022-08-09\" }"

🧪 Run tests
pytest -v

🛠 Tech Stack

Python 3.12

Flask

Requests

Fastavro

Pytest

PEP8 & type hints

👨‍💻 Author

Ruslan Konyk
