from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """Fetches the current weather for a given location."""
    # Placeholder implementation; in a real scenario, you would fetch data from a weather API.
    return "Raining"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")

