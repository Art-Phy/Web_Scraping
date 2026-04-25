
import csv


def export_to_csv(results: list[dict[str, str]], output_path: str) -> None:
    """
    Exports extracted link results to a CSV file.
    """
    fieldnames = ["text", "href"]

    with open(output_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
