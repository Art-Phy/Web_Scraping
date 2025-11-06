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
from beautifulsoup4 import BeautifulSoup
import argparse
from pathlib import Path

def extraer_textos(url: str, palabra: str) ->list[str]:
    
