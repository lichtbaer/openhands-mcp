from fastmcp import FastMCP

from app.config import MCP_CONFIG

mcp = FastMCP("MCP Template Server")

if __name__ == "__main__":
    mcp.run(host=MCP_CONFIG["server_host"], port=MCP_CONFIG["server_port"], debug=MCP_CONFIG["debug"])
