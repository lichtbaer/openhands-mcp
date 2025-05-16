# Microagent: FastMCP

## Beschreibung
FastMCP ist eine Python-Bibliothek zur schnellen Entwicklung von MCP-Servern, die speziell für die Interaktion mit OpenHands-Agents und Microagents ausgelegt sind. Sie implementiert das Model Context Protocol (MCP) und bietet eine flexible, modulare Architektur für KI- und Datenanwendungen.

## Grundlegende Nutzung

```python
from fastmcp.server import MCPServer

app = MCPServer()

@app.resource()
def hello_world(ctx):
    return {"message": "Hello, MCP!"}

if __name__ == "__main__":
    app.run()
```

## Fortgeschrittene Techniken

### Authentifizierung
FastMCP unterstützt verschiedene Authentifizierungsmechanismen. Beispiel für einen einfachen API-Key-Check:

```python
from fastmcp.auth import api_key_auth

app = MCPServer(auth=api_key_auth(["MEIN_API_KEY"]))
```

Für komplexere Szenarien können eigene Auth-Handler implementiert werden.

### OpenAPI-Codegenerierung
FastMCP kann OpenAPI-Spezifikationen nutzen, um automatisch Endpunkte und Datenmodelle zu generieren:

```python
from fastmcp.openapi import import_openapi

import_openapi(app, "./openapi.yaml")
```

Dadurch werden alle in der OpenAPI-Datei definierten Ressourcen automatisch als Endpunkte bereitgestellt.

### Containerisierung & Deployment
- FastMCP-Server können einfach in Docker-Containern betrieben werden.
- Für produktive Deployments sollten Umgebungsvariablen und Secrets genutzt werden (z.B. für API-Keys).

### Weitere Hinweise
- Siehe [FastMCP Dokumentation](https://gofastmcp.com) für Details zu Ressourcen, Tools, Prompts und fortgeschrittenen Features.
- Das MCP-Protokoll ist unter [modelcontextprotocol.io](https://modelcontextprotocol.io/introduction) dokumentiert.
