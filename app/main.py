import json
import httpx
from fastmcp import FastMCP
from app.config import MCP_CONFIG

with open(MCP_CONFIG["openapi_spec_path"], "r") as f:
    openapi_spec = json.load(f)

api_client = httpx.AsyncClient(base_url=MCP_CONFIG["api_base_url"])
mcp = FastMCP.from_openapi(openapi_spec=openapi_spec, client=api_client, name="OpenHands API")

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host=MCP_CONFIG["server_host"], port=MCP_CONFIG["server_port"], log_level="debug")
