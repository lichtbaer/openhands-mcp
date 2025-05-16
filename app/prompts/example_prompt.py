"""
Beispiel-Prompt für das MCP Template Projekt.
"""
from fastmcp import prompt

@prompt()
def greet(name: str) -> str:
    """Erzeugt eine Begrüßung für den angegebenen Namen."""
    return f"Hallo, {name}! Willkommen beim MCP Template."
