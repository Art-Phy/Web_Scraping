
from bs4 import BeautifulSoup


def extract_matching_links(html: str, keyword: str) -> list[str]:
    """
    Extrae los textos de los enlaces <a> cuyo contenido tiene la palabra clave indicada.
    """
    soup = BeautifulSoup(html, "html.parser")
    results: list[str] = []

    for link in soup.find_all("a"):
        text = link.get_text(strip=True)
        if keyword.lower() in text.lower():
            results.append(text)

    return results
