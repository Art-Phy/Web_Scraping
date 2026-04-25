
import argparse

from web_scraping.fetcher import fetch_html
from web_scraping.parser import extract_matching_links
from web_scraping.exporter import export_to_csv



def  build_parser() -> argparse.ArgumentParser:
    """
    Crea y configura el parser de argumentos de la CLI
    """
    parser = argparse.ArgumentParser(
        description="Extract links from a web page whose text matches a keyword."
    )
    parser.add_argument("url", help="URL of the page to analyze")
    parser.add_argument("keyword", help="Keyword to search for in link text")
    parser.add_argument(
         "--csv",
         dest="csv_path",
         help="Export results to a CSV file",
    )
    return parser



def print_results(results: list[dict[str, str]]) -> None:
        print("\nMatches found:\n")
        for index, result in enumerate(results, start=1):
            print(f"{index}. Text: {result['text']}")
            print(f"    URL: {result['href']}\n")



def run() -> None:
    """
    Ejecuta el flujo principal
    """
    parser = build_parser()
    args = parser.parse_args()

    try:
        html = fetch_html(args.url)
        results = extract_matching_links(html, args.keyword, args.url)

        if results:
            print_results(results)
            if args.csv_path:
                export_to_csv(results, args.csv_path)
                print(f"Resutls exported to CSV: {args.csv_path}")
        else:
            print("\nNo matches found.")

    except Exception as exc:
        print(f"\nError: {exc}")
