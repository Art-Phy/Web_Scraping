### Web Scraping CLI 🕸️

<p align="left">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/CLI-Web%20Scraper-orange" />
  <img src="https://img.shields.io/badge/BeautifulSoup-HTML%20Parsing-green" />
  <img src="https://img.shields.io/badge/Status-v0.2.0%20Stable-success" />
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

---

#### CLI Features

- Interfaz de línea de comandos basada en `argparse`.
- Entrada de URL y keyword como argumentos.
- Salida formateada y numerada.
- Manejo básico de errores (peticiones HTTP, parsing, etc.).
- Exportación a **CSV** y a **JSON**

---

#### 📊 Ejemplo de uso

```bash
PYTHONPATH=src python3 -m web_scraping.main "https://example.com" "blog"

PYTHONPATH=src python3 -m web_scraping.main "https://exmple.com" "blog" --csv results.csv --json results.json
```

---

#### 🛠️ Stack tecnológico
- Lenguaje: Python
- HTTP: requests
- Parsing HTML: BeautifulSoup
- CLI: argparse
- Control de versiones: Git + GitFlow

---

#### 🧠 Decisiones técnicas destacables
- Separación de responsabilidades en módulos:
    * fetcher → descarga HTML
    * parser → extracción de enlaces
    * cli → interfaz de usuario
- Arquitectura basada en src/ para mayor escalabilidad.
- Uso de argparse para una CLI simple y extensible.
- Uso de headers personalizados para evitar bloqueos básicos.
- Manejo de errores para mejorar la experiencia de uso.
- Diseño ligero orientado a herramientas reales.
- Preparado para ampliaciones sin romper estructura.
- Versionado semántico con releases.
- Flujo GitFlow (main, develop, feature/*).
- Exportación de resultados a CSV / JSON
- Mostrar también URLs (href) además del texto

---

#### 🔭 Posibles extensiones futuras (no implementadas)
- Límite de resultados (--limit)
- Soporte para múltiples keywords
- Logging estructurado
- Tests automatizados con pytest

---

#### 📁 Project Structure
```
Web_Scraping
├── CHANGELOG.md
├── LICENSE.md
├── README.md
├── requirements.txt
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
