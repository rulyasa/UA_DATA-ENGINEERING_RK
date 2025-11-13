import os
from flask import Flask, request
from flask.typing import ResponseReturnValue

from bll.sales_api import save_sales_to_local_disk

app = Flask(__name__)


@app.post("/")
def handle_request() -> ResponseReturnValue:
    """Entry point for running job #1 via POST request."""
    data = request.get_json()

    date: str | None = data.get("date")
    raw_dir: str | None = data.get("raw_dir")

    if not date or not raw_dir:
        return {"message": "date and raw_dir are required"}, 400

    save_sales_to_local_disk(date=date, raw_dir=raw_dir)
    return {"message": "Data retrieved successfully"}, 201


def _check_env() -> None:
    """Ensure AUTH_TOKEN is set."""
    if "AUTH_TOKEN" not in os.environ:
        raise EnvironmentError("AUTH_TOKEN environment variable must be set")


if __name__ == "__main__":
    _check_env()
    app.run(host="localhost", port=8081, debug=False)
