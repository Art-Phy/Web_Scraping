### Web Scraping ###

# Importamos los módulos necesarios
import requests
from bs4 import BeautifulSoup

# Indicamos la URL de la web que queramos
url = "https://valenciasecreta.com/restaurantes-valencia/"

# Añadimos get
respuesta = requests.get(url)

# Comprobamos si la petición funcionó
if respuesta.status_code == 200:
    # Creamos una instancia con el contenido de la página
    soup = BeautifulSoup(respuesta.content, "html.parser")

    # Le decimos que encuentre los enlaces <a> que pueden contener los nombres de los restaurantes
    restaurantes = soup.find_all('a')

    # Creamos una lista para almacenar los nombres de los restaurantes
    restaurante_lista = []

    # Iteramos sobre los enlaces y extrae el texto asociado a nuestra palabra
    for restaurante in restaurantes:
        if restaurante.get_text():
            if "restaurante" in restaurante.get_text().lower():
                restaurante_lista.append(restaurante.get_text().strip())
        
    # Muestra los resultados
    print("\nLos restaurantes encontrados son: ")
    for i, rest in enumerate(restaurante_lista, 1):
        print(f"{i}. {rest}")
else:
    print(f"Algo no ha ido bien. {respuesta.status_code}")
