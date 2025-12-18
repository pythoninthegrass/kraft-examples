"""ArXiv MCP Server Python Client
-----------------------------

This script demonstrates how to connect to an ArXiv MCP server deployed on Unikraft Cloud using Streamable HTTP transport.
It lists available tools and performs a sample search for papers using the MCP protocol.

Usage:
    export MCP_SERVER_URL=https://your-server-url/mcp
    uv run client.py
"""
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "fastmcp",
# ]
# ///

import asyncio
import os
from fastmcp import Client


async def main():
    url = os.getenv("MCP_SERVER_URL", None)
    if url is None:
        print("Error: MCP_SERVER_URL environment variable is not set.")
        print("Please set it to the server's MCP endpoint URL (e.g., https://your-server-url/mcp).")
        return

    print(f"Connecting to {url}...")

    try:
        async with Client(url) as client:
            # List available tools
            print("\n--- Listing Tools ---")
            tools = await client.list_tools()
            for tool in tools:
                print(f"Name: {tool.name}")
                print(f"Description: {tool.description}")
                print()

            # Example: Search for papers
            print("\n--- Searching for 'unikraft' ---")
            try:
                result = await client.call_tool(
                    "search_papers",
                    arguments={"query": "unikraft", "max_results": 3}
                )
                for content in result.content:
                    if content.type == "text":
                        print(content.text)

            except Exception as e:
                print(f"Error calling tool: {e}")

    except Exception as e:
        print(f"Connection error: {e}")
        print("Make sure the URL is correct and the server is running.")


if __name__ == "__main__":
    asyncio.run(main())
