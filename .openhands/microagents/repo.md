# MCP Template Projekt

Dieses Projekt dient als Template für MCP Server, die auf dem Model Context Protocol (MCP) und der FastMCP-Bibliothek basieren. Ziel ist es, eine einheitliche, modulare und klar dokumentierte Architektur für containerisierte HTTP-basierte Applikationen bereitzustellen.

## Projektziele
- **Wiederverwendbarkeit:** Klare Struktur und Modularisierung für verschiedene MCP-Server.
- **Standardisierung:** Einheitliche Schnittstellen und Komponenten.
- **Containerisierung:** Bereitstellung als Docker-Container.
- **Erweiterbarkeit:** Einfache Integration neuer Ressourcen, Tools und Prompts.

## Architekturüberblick
- **FastMCP:** High-Level Python-Framework zur schnellen Entwicklung von MCP-Servern.
- **MCP-Protokoll:** Standardisierte Schnittstelle für LLM-Interaktionen (siehe [modelcontextprotocol.io](https://modelcontextprotocol.io/introduction)).
- **HTTP-API:** Kommunikation erfolgt ausschließlich über HTTP.
- **Microagents:** Kleine, klar abgegrenzte Module für spezifische Aufgaben.

## Verzeichnisstruktur (Empfehlung)

```
/ (Projektwurzel)
│
├── app/                  # Hauptapplikation (FastMCP-Server, Ressourcen, Tools, Prompts)
│   ├── __init__.py
│   ├── main.py           # Einstiegspunkt
│   ├── resources/        # MCP-Ressourcen (z.B. Datenquellen)
│   ├── tools/            # MCP-Tools (z.B. Aktionen, Funktionen)
│   ├── prompts/          # MCP-Prompts (Vorlagen für LLM-Interaktionen)
│   └── config.py         # Konfiguration
│
├── microagents/          # Microagent-Module (optional, für Erweiterungen)
│   └── ...
│
├── tests/                # Tests für Ressourcen, Tools, Prompts, Microagents
│
├── Dockerfile            # Container-Build
├── requirements.txt      # Python-Abhängigkeiten
├── README.md             # Hauptdokumentation
└── .openhands/
    └── microagents/
        └── repo.md       # (Diese Datei)
```

## Microagents
Microagents sind kleine, spezialisierte Module, die bestimmte Aufgaben übernehmen (z.B. Datenzugriff, Transformation, externe API-Anbindung). Sie werden im Verzeichnis `microagents/` abgelegt und können einfach in die Hauptapplikation integriert werden.

### Beispiele für Microagents
- **Datenbankzugriff** (z.B. PostgreSQL, SQLite)
- **Datei-Import/Export**
- **Externe API-Integration**
- **Daten-Transformation**

## Weiterführende Links
- [FastMCP Dokumentation](https://gofastmcp.com)
- [MCP Protokoll](https://modelcontextprotocol.io/introduction)

## Hinweise
- Jeder Microagent sollte eine eigene README oder docstring-Dokumentation enthalten.
- Die Hauptdokumentation befindet sich in der `README.md` im Projektwurzelverzeichnis.
