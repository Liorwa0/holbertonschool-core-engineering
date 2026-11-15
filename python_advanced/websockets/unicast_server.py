#!/usr/bin/env python3
"""A WebSocket server that sends each message only to its sender."""

import asyncio

import websockets
from websockets.exceptions import ConnectionClosed


connected_clients = set()


async def connection_handler(websocket):
    """Register a client and reply only on its own connection."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the unicast WebSocket server."""
    async with websockets.serve(
        connection_handler, "127.0.0.1", 8765
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
