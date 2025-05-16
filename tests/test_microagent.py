import pytest
from fastmcp import FastMCP
import httpx
import json

@pytest.fixture(scope="module")
def mcp_server():
    from app.config import MCP_CONFIG
    from app.main import mcp
    yield mcp

def test_resource_template_generation(mcp_server):
    # Check that resource templates are generated for path params
    templates = mcp_server.resource_templates
    assert isinstance(templates, dict)
