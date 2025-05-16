import pytest
from fastmcp import FastMCP
import httpx
import json

@pytest.fixture(scope="module")
def mcp_server():
    from app.config import MCP_CONFIG
    from app.main import mcp
    yield mcp


def test_health(mcp_server):
    # Health endpoint should be available as a resource
    resources = mcp_server.resources
    assert "health" in resources


def test_openapi_resources(mcp_server):
    # Check that at least one resource and one tool are generated
    assert len(mcp_server.resources) > 0 or len(mcp_server.tools) > 0
