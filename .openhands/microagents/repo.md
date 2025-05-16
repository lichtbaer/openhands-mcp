# MCP Server Template – Microagents Grundsätze

Dieses Projekt ist ein OpenHands-kompatibler MCP-Server, der als Template für die Entwicklung von modularen, containerisierten und klar strukturierten MCP-Servern dient. Ziel ist die nahtlose Interaktion mit OpenHands-Agents und -Microagents über das Model Context Protocol (MCP) und FastMCP.

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
