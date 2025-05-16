# MCP Server Template – Microagents Grundsätze

Dieses Projekt dient als Template für MCP-Server auf Basis von FastMCP und dem Model Context Protocol (MCP). Ziel ist eine klare, modulare und containerisierte Architektur für die Entwicklung von MCP-Servern.

## Grundsätze
- **Modularität:** Trennung von Ressourcen, Tools und Prompts für maximale Wiederverwendbarkeit.
- **Klarheit:** Einheitliche Verzeichnisstruktur und Dokumentation für schnellen Einstieg und Wartbarkeit.
- **Sicherheit:** Integration von Linting (Ruff) und Security-Checks (Bandit) im Entwicklungsprozess.
- **Containerisierung:** Bereitstellung als Docker-Container für einfache Deployments.
- **Erweiterbarkeit:** Microagents können als eigenständige, wiederverwendbare Module entwickelt und dokumentiert werden.

## Verzeichnisstruktur (Auszug)

```
/ (Projektwurzel)
│
├── app/            # Hauptapplikation (FastMCP-Server, Ressourcen, Tools, Prompts)
├── tests/          # Tests
├── Dockerfile      # Container-Build
├── requirements.txt
├── .openhands/     # Automatisierung, Hooks, Microagents-Doku
│   └── microagents/
│       ├── repo.md         # Diese Datei: Grundsätze & Übersicht
│       └── fastmcp.md      # Nutzungshinweise zu FastMCP
```

## Microagents
Microagents sind kleine, wiederverwendbare Module, die spezifische Aufgaben übernehmen (z.B. Datenbankzugriffe, API-Integrationen, Daten-Transformationen). Sie werden dokumentiert und können in anderen Projekten wiederverwendet werden.

Jeder Microagent sollte eine eigene Dokumentation (README oder docstring) enthalten.
