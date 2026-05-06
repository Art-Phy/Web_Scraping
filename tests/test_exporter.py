
import json
import csv
import os

from web_scraping.exporter import export_to_csv, export_to_json



def test_export_to_csv(tmp_path):
    results = [
        {"text": "Blog", "href": "https://example.com/blog"}
    ]

    file_path = tmp_path / "test.csv"

    export_to_csv(results, file_path)

    assert os.path.exists(file_path)

    with open(file_path, newline="", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        assert reader[0]["text"] == "Blog"
        assert reader[0]["href"] == "https://example.com/blog"



def text_export_to_json(tmp_path):
    results = [
        {"text": "Blog", "href": "https://example.com/blog"}
    ]

    file_path = tmp_path / "test.json"

    export_to_json(results, file_path)

    assert os.path.exists(file_path)

    with open(file_path, newline="", encoding="utf-8") as f:
        data = json.load(f)
        assert data[0]["text"] == "Blog"
        assert data[0]["href"] == "https://example.com/blog"
