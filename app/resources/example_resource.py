"""
Beispiel-Resource für das MCP Template Projekt.
"""
from fastmcp import resource

@resource()
def hello_world():
    """Gibt eine Beispiel-Nachricht zurück."""
    return {"message": "Hello, MCP World!"}
