
import html
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def clean_text(text: str) -> str:
    """
    Cleans extracted text by:
        - Unescaping HTML entities
        - Removing extra whitespace
        - Normalizing problematic characters
    """
    text = html.unescape(text)
    text = text.replace("\xa0", " ") # non-breaking space
    text = text.strip()

    return text



def extract_matching_links(html: str, keyword: str, base_url: str) -> list[dict[str, str]]:
    """
    Extrae los textos de los enlaces <a> cuyo contenido tiene la palabra clave indicada.
    Devuelve una lista de diccionarios con el texto y la URL absoluta.
    """
    soup = BeautifulSoup(html, "html.parser")
    results: list[dict[str, str]] = []

    for link in soup.find_all("a"):
        raw_text = link.get_text()
        text = clean_text(raw_text)
        href = link.get("href")

        if not text or not href:
            continue

        if keyword.lower() in text.lower():
            absolute_url = urljoin(base_url, href)
            results.append(
                {
                    "text": text,
                    "href": absolute_url,
                }
            )

    return results
