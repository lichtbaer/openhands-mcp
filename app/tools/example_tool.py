"""
Beispiel-Tool für das MCP Template Projekt.
"""
from fastmcp import tool

@tool()
def add(a: int, b: int) -> int:
    """Addiert zwei Zahlen."""
    return a + b
