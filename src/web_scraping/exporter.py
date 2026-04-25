
import csv
import json



def export_to_csv(results: list[dict[str, str]], output_path: str) -> None:
    """
    Exports extracted link results to a CSV file.
    """
    fieldnames = ["text", "href"]

    with open(output_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)



def export_to_json(results: list[dict[str, str]], output_path: str) -> None:
    """
    Exports extracted link results to a JSON file.
    """
    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(results, json_file, indent=4, ensure_ascii=False)
