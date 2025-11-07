"""
======================
WEB SCRAPING (V1.1.0)
======================

Script genérico para realizar Web Scraping y listar los texto de los enlaces <a> 
que contengan la palabra clave indicada por el usuario.

Autor: Art-Phy
Require: requests, beatifulsoup4
"""

import requests
from bs4 import BeautifulSoup
import argparse
import sys



def obtener_html(url: str) -> str:
    """
    Descarga el HTML de la URL proporcionada.

    Args:
        url: dirección web completa.

    Returns:
        HTML de la página como string o cadena vacía si falla.
    """
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/121.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "es-ES,es;q=0.9",
        }
        respuesta = requests.get(url, headers=headers, timeout=10)
        if respuesta.status_code == 200:
            return respuesta.text
        else:
            print(f"[!] Error: respuesta HTTP {respuesta.status_code}")
            return ""
    except requests.RequestException as e:
        print(f"[!] Error de conexión: {e}")
        return ""


def buscar_enlaces(html: str, palabra_clave: str) -> list[str]:
    """
    Busca enlaces <a> cuyo texto contenga la palabra clave.

    Args:
        html: contenido HTML de la página.
        palabra_clave: texto a buscar (minúsculas).

    Returns:
        Lista con los textos encontrados.
    """
    soup = BeautifulSoup(html, "html.parser")
    enlaces = soup.find_all("a")
    resultados = []

    for enlace in enlaces:
        texto = enlace.get_text(strip=True)
        if texto and palabra_clave.lower() in texto.lower():
            resultados.append(texto)
    return resultados


def main() -> None:
    parser = argparse.ArgumentParser(description="Buscador genérico de enlaces en páginas web.")
    parser.add_argument("-u", "--url", help="URL completa de la web a analizar.")
    parser.add_argument("-k", "--keyword", help="Palabra clave a buscar en los enlaces.")
    args = parser.parse_args()

    # Pedir datos si no se pasaron por argumento
    while not args.url:
        args.url = input("Introduce la URL (o escribe 'salir' para terminar): ").strip()
        if args.url.lower() == "salir":
            sys.exit("Saliendo del programa...")

    if not args.keyword:
        args.keyword = input("Introduce la palabra clave a buscar: ").strip()

    print(f"\n🔍 Analizando: {args.url}")
    html = obtener_html(args.url)

    # Si el HTML parece vacío o no contiene texto visible
    if not html or len(html) < 500:
        print("\n⚠️  El contenido HTML parece vacío o muy corto.")
        print("   Esto puede deberse a que la página usa JavaScript para cargar el contenido dinámicamente.")
        print("   Prueba con librerías como `requests_html` o `selenium` para obtener el contenido real.\n")
        sys.exit()

    resultados = buscar_enlaces(html, args.keyword)

    if resultados:
        print("\n✅ Resultados encontrados:")
        for i, texto in enumerate(resultados, 1):
            print(f"{i}. {texto}")
    else:
        print("\n⚠️ No se encontraron coincidencias.")
        print("   Es posible que el contenido se cargue dinámicamente o que la palabra no aparezca en los enlaces.")


if __name__ == "__main__":
    main()
