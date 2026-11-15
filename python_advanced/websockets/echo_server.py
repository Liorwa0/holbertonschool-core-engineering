#!/usr/bin/env python3
"""A simple WebSocket server that echoes client messages."""

import asyncio

import websockets


async def connection_handler(websocket):
    """Echo every text message received from a client."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the WebSocket echo server."""
    async with websockets.serve(
        connection_handler, "127.0.0.1", 8765
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
