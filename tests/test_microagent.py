import pytest

@pytest.fixture(scope="module")
def mcp_server():
    from app.main import mcp
    yield mcp

def test_resource_template_generation(mcp_server):
    # Check that resource templates are generated for path params
    templates = mcp_server.resource_templates
    assert isinstance(templates, dict)
