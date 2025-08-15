from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("hello-mcp")

@mcp.tool()
def echo(text: str) -> str:
    """Echo back the provided text."""
    return text

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers and return the sum."""
    return a + b


@mcp.tool()
async def sum_gxo(a: float, b: float) -> float:
    """Sum two numbers and return the sum the gxo way."""
    async with httpx.AsyncClient() as client:
        r = await client.post("http://127.0.0.1:8000/sum", json={"a": a, "b": b})
        r.raise_for_status()
        return r.json()["sum"]

if __name__ == "__main__":
    mcp.run()