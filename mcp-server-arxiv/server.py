"""This wrapper sets up an SSE server for the MCP server using Starlette and Uvicorn."""

import logging
import uvicorn
from mcp.server.sse import SseServerTransport
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import Response
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions
from arxiv_mcp_server.server import server, settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("arxiv-mcp-server-sse")

sse = SseServerTransport("/messages")


async def handle_health(request: Request):
    """Handle health check requests."""
    return Response("OK")


async def handle_sse(request: Request):
    """Handle incoming SSE connections and initialize the MCP server transport."""
    async with sse.connect_sse(
        request.scope, request.receive, request._send
    ) as streams:
        await server.run(
            streams[0],
            streams[1],
            InitializationOptions(
                server_name=settings.APP_NAME,
                server_version=settings.APP_VERSION,
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(resources_changed=True),
                    experimental_capabilities={},
                ),
            ),
        )


async def handle_messages(request: Request):
    """Handle incoming POST messages for the SSE transport."""
    try:
        result = await sse.handle_post_message(request.scope, request.receive, request._send)
        if result is None:
            return Response(status_code=202)  # Accepted
        return result
    except Exception as e:
        logger.error("Error handling message: %s", e)
        return Response(f"Error: {e}", status_code=500)


app = Starlette(
    routes=[
        Route("/", endpoint=handle_health),
        Route("/health", endpoint=handle_health),
        Route("/sse", endpoint=handle_sse),
        Route("/messages", endpoint=handle_messages, methods=["POST"]),
    ]
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
