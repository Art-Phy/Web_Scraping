## 🧾 CHANGELOG

All notable changes to this project will be documented in this file.

---

### [0.2.0] - 25.04.2026

#### Added
- Structured link extraction (text + href)
- CSV export support
- JSON export support
- Absolute URL resolution for links

#### Improved
- CLI output formatting

#### Refactored
- Parser now returns structured data instead of plain text
- Export logic moved to dedicated module

---

### [0.1.0] - 21.04.2026

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
