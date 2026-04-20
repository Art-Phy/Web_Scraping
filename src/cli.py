
import argparse

from src.fetcher import fetch_html
from src.parser import extract_matching_links



def  build_parser() -> argparse.ArgumentParser:
    """
    Crea y configura el parser de argumentos de la CLI
    """
    parser = argparse.ArgumentParser(
        description="Busca enlaces que contengan una palabra clave dentro de una web"
    )
    parser.add_argument("url", help="URL de la página a analizar")
    parser.add_argument("keyword", help="Palabra clave a buscar en los enlaces")
    return parser



def run() -> None:
    """
    Ejecuta el flujo principal
    """
    parser = build_parser()
    args = parser.parse_args()

    try:
        html = fetch_html(args.url)
        results = extract_matching_links(html, args.keyword)

        if results:
            print("\nCoincidencias encontradas:")
            for index, result in enumerate(results, start=1):
                print(f"{index}, {result}")

        else:
            print("\nNo se encontraron coincidencias.")

    except Exception as exc:
        print(f"\nError: {exc}")
