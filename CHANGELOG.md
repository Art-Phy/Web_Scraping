## 🧾 CHANGELOG

### [1.1.1] - 2025-11-03
#### Mejoras
- Se eliminó la URL por defecto: ahora el usuario debe introducir una manualmente.
- Se corrigió el error `NameError: name 'sys' is not defined` añadiendo `import sys`.
- Se añadió un `User-Agent` más completo para evitar bloqueos por parte de servidores web.
- Se implementaron mensajes más claros para manejar errores HTTP (403, 404, etc.).
- El script ahora avisa si una página usa contenido dinámico (JavaScript) y recomienda `requests_html` o `selenium`.

#### Planificado para próxima versión (v1.2.0)
- Compatibilidad con sitios que cargan contenido mediante JavaScript (uso de `requests_html` o `selenium`).
- Posibilidad de exportar los resultados encontrados a un archivo `.txt` o `.csv`.
- Mejora del rendimiento al buscar múltiples palabras clave simultáneamente.
