import sys
import os
import pytest
from unittest.mock import patch

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)


@pytest.fixture
def mock_sales_api():
    """Mock API responses for job1."""
    pages = {
        1: [{"client": "A", "purchase_date": "2022-08-09",
             "product": "TV", "price": 100}],
        2: [{"client": "B", "purchase_date": "2022-08-09",
             "product": "Phone", "price": 200}],
        3: [{"client": "C", "purchase_date": "2022-08-09",
             "product": "Laptop", "price": 300}],
        4: [{"client": "D", "purchase_date": "2022-08-09",
             "product": "Tablet", "price": 400}],
    }

    def mock_fetch(date: str, page: int):
        return pages.get(page)

    with patch("job1.bll.sales_api.fetch_sales_page", side_effect=mock_fetch):
        yield
