# MCP Template Projekt

Dieses Projekt ist ein Template für MCP-Server auf Basis von [FastMCP](https://gofastmcp.com) und dem [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction). Es bietet eine standardisierte, modulare und containerisierte Architektur für die Entwicklung von MCP-Servern.

## Ziele
- **Schneller Einstieg:** Klare Struktur und Dokumentation für neue Projekte.
- **Modularität:** Trennung von Ressourcen, Tools, Prompts und Microagents.
- **Wiederverwendbarkeit:** Microagents und Module können einfach in anderen Projekten genutzt werden.
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
├── microagents/          # Microagent-Module (optional)
│   └── ...
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
- **microagents/**: Erweiterbare, kleine Module für spezifische Aufgaben.
- **tests/**: Tests für alle Module und Microagents.
- **Dockerfile**: Für die Containerisierung.
- **requirements.txt**: Listet alle Python-Abhängigkeiten.

## Microagents
Microagents sind kleine, wiederverwendbare Module, die z.B. für Datenbankzugriffe, API-Integrationen oder Daten-Transformationen genutzt werden können. Sie werden im Verzeichnis `microagents/` abgelegt und in der `.openhands/microagents/repo.md` dokumentiert.

## Weiterführende Links
- [FastMCP Dokumentation](https://gofastmcp.com)
- [MCP Protokoll](https://modelcontextprotocol.io/introduction)

## Hinweise
- Jeder Microagent sollte eine eigene Dokumentation (README oder docstring) enthalten.
- Die Hauptdokumentation befindet sich in dieser Datei.
