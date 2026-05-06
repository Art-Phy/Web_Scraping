### Web Scraping CLI 🕸️

<p align="left">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/CLI-Web%20Scraper-orange" />
  <img src="https://img.shields.io/badge/BeautifulSoup-HTML%20Parsing-green" />
  <img src="https://img.shields.io/badge/pytest-Tested-blueviolet" />
  <img src="https://img.shields.io/badge/Status-v0.4.0%20Stable-success" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />
</p>

Herramienta **CLI desarrollada en Python** que permite analizar una página web y extraer enlaces (`<a>`) cuyo texto contiene una palabra clave específica.

---

### ✨ Funcionalidades

#### Core

- Descarga de contenido HTML desde cualquier URL.
- Parsing de HTML mediante **BeautifulSoup**.
- Extracción de enlaces `<a>`.
- Filtrado por palabra clave (case-insensitive).
- Conversión automática de enlaces relativos a URLs absolutas.
- Limpieza básica de texto y manejo de encoding.

---

#### CLI Features

- Interfaz de línea de comandos basada en `argparse`.
- Entrada de URL y keyword como argumentos.
- Salida formateada y numerada.
- Manejo básico de errores (peticiones HTTP, parsing, etc.).
- Exportación a **CSV** y **JSON**.
- Limitación de resultados mediante `--limit`.
- Validación de argumentos CLI.

---

#### 📊 Ejemplo de uso

```bash
PYTHONPATH=src python3 -m web_scraping.main "https://example.com" "blog"

PYTHONPATH=src python3 -m web_scraping.main "https://example.com" "blog" --limit 3

PYTHONPATH=src python3 -m web_scraping.main "https://example.com" "blog" --csv results.csv --json results.json

PYTHONPATH=src python3 -m web_scraping.main "https://example.com" "blog" --limit 2 --csv results.csv
```

---

#### 🛠️ Stack tecnológico
- Lenguaje: Python
- HTTP: requests
- Parsing HTML: BeautifulSoup
- CLI: argparse
- Testing: pytest
- Control de versiones: Git + GitFlow

---

#### 🧠 Decisiones técnicas destacables
- Separación de responsabilidades en módulos:
    * fetcher → descarga HTML
    * parser → extracción de enlaces
    * cli → interfaz de usuario
    * exporter -> exportación de datos.
- Arquitectura basada en **src/** para mayor escalabilidad.
- Uso de **argparse** para una CLI simple y extensible.
- Uso de headers personalizados para evitar bloqueos básicos.
- Manejo de errores para mejorar la experiencia de uso.
- Diseño ligero orientado a herramientas reales.
- Preparado para ampliaciones sin romper estructura.
- Versionado semántico con releases.
- Flujo GitFlow (main, develop, feature/*).
- Exportación de resultados a CSV / JSON.
- Conversión automática de URLs relativas.
- Limpieza de texto para reducir artefactos de enconding.
- Tests automatizados para parser y exportación.

---

#### 🧪 Testing
```
PYTHONPATH=src pytest
```
---

#### 🔭 Posibles extensiones futuras (no implementadas)
- Soporte para múltiples keywords
- Logging estructurado
- Test de integración para CLI
- Mocking de requests HTTP
- Soporte para scraping dinámico con JavaScript

---

#### 📁 Project Structure
```
Web_Scraping
├── CHANGELOG.md
├── LICENSE.md
├── README.md
├── requirements.txt
├── tests
│   ├── test_basic.py
│   ├── test_exporter.py
│   └── test_parser.py
└── src
    └── web_scraping
        ├── cli.py
        ├── exporter.py
        ├── fetcher.py
        ├── main.py
        └── parser.py
```

---
> [!TIP]
> ###### Si consideras útil el repositorio, puedes apoyarlo dejando una ⭐
