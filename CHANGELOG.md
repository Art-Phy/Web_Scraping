## 🧾 CHANGELOG

### [0.1.0] - 21.04.2026

All notable changes to this project will be documented in this file.

---

#### Added

* Project structure using `src/` layout
* Modular architecture (fetcher, parser, cli, main)
* Command-line interface with argparse
* HTML fetching with custom headers and timeout
* Link extraction with keyword filtering

#### Refactored

* Split original monolithic script into separate modules

#### Removed

* Legacy `scraping.py` script
* Cached Python files (`__pycache__`)
