# MCP Template Projekt

## Pre-Commit Hook
## Setup

Für die lokale Entwicklung und Tests:

```bash
. ./.openhands/setup.sh
```

Für den Produktivbetrieb (z.B. im Docker-Container) werden nur die Pakete aus `requirements.txt` installiert.



Vor jedem Commit wird automatisch ein Check mit [Ruff](https://github.com/astral-sh/ruff) (Code Style/Linting) und [Bandit](https://github.com/PyCQA/bandit) (Security) durchgeführt. Das Skript befindet sich unter `.openhands/pre-commit.sh` und kann als Git-Hook eingebunden werden:

```bash
ln -s ../../.openhands/pre-commit.sh .git/hooks/pre-commit
```

**Hinweis:** Bandit meldet einen Sicherheitshinweis, wenn der Server auf `0.0.0.0` gebunden wird (siehe `app/config.py`). Dies ist für containerisierte Umgebungen und Entwicklung meist gewollt, sollte aber für Produktionsumgebungen geprüft werden.


Dieses Projekt ist ein Template für MCP-Server auf Basis von [FastMCP](https://gofastmcp.com) und dem [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction). Es bietet eine standardisierte, modulare und containerisierte Architektur für die Entwicklung von MCP-Servern.

## Ziele
- **Schneller Einstieg:** Klare Struktur und Dokumentation für neue Projekte.
- **Modularität:** Trennung von Ressourcen, Tools und Prompts.
- **Wiederverwendbarkeit:** Module können einfach in anderen Projekten genutzt werden.
- **Containerisierung:** Bereitstellung als Docker-Container für einfache Deployment-Prozesse.

## Verzeichnisstruktur

```
/ (Projektwurzel)
│
├── app/                  # Hauptapplikation (FastMCP-Server, Ressourcen, Tools, Prompts)
│   ├── __init__.py
│   ├── main.py           # Einstiegspunkt
│   ├── resources/        # MCP-Ressourcen
│   ├── tools/            # MCP-Tools
│   ├── prompts/          # MCP-Prompts
│   └── config.py         # Konfiguration
│
├── tests/                # Tests
│
├── Dockerfile            # Container-Build
├── requirements.txt      # Python-Abhängigkeiten
├── README.md             # (Diese Datei)
└── .openhands/
    └── microagents/
        └── repo.md       # Projektbeschreibung und Microagents
```

## Komponenten
- **app/**: Enthält die Hauptlogik des MCP-Servers (Ressourcen, Tools, Prompts).
- **tests/**: Tests für alle Module.
- **Dockerfile**: Für die Containerisierung.
- **requirements.txt**: Listet alle Python-Abhängigkeiten.

## Weiterführende Links
- [FastMCP Dokumentation](https://gofastmcp.com)
- [MCP Protokoll](https://modelcontextprotocol.io/introduction)

## Hinweise
- Die Hauptdokumentation befindet sich in dieser Datei.
