# Konfigurationsdatei für das MCP Template Projekt

import os
from dotenv import load_dotenv

load_dotenv()

MCP_CONFIG = {
    "server_host": "0.0.0.0",
    "server_port": 54185,
    "debug": True,
    "api_base_url": os.getenv("OPENHANDS_API_BASE_URL", "http://localhost:3000"),  # Ziel-API-Basis-URL
    "openapi_spec_path": "api/openapi.json"   # Pfad zur OpenAPI-Spezifikation
}
