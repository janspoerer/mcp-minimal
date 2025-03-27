from mcp.server.fastmcp import FastMCP
import datetime

# Initialize FastMCP server
mcp = FastMCP("mcp-minimal")

# Store browser sessions
browser_sessions = {}

@mcp.tool()
async def get_date_andtime() -> str:
    """Gets the current date and time

    Args:
        No arguments available
    """

    return str(datetime.datetime.now())

if __name__ == "__main__":
    # Initialize and run the server with stdio transport
    print("Starting MCP server (minimal version)...", flush=True)
    mcp.run(transport='stdio')
