import os
from flask import Flask, request
from flask.typing import ResponseReturnValue

from bll.converter import convert_json_to_avro

app = Flask(__name__)


@app.post("/")
def handle_request() -> ResponseReturnValue:
    """Entry point for conversion job."""
    data = request.get_json()

    raw_dir: str | None = data.get("raw_dir")
    stg_dir: str | None = data.get("stg_dir")

    if not raw_dir or not stg_dir:
        return {"message": "raw_dir and stg_dir are required"}, 400

    convert_json_to_avro(raw_dir=raw_dir, stg_dir=stg_dir)
    return {"message": "Converted successfully"}, 201


if __name__ == "__main__":
    app.run(host="localhost", port=8082, debug=False)
