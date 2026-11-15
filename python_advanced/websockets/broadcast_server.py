#!/usr/bin/env python3
"""A WebSocket server that broadcasts messages to all clients."""

import asyncio

import websockets
from websockets.exceptions import ConnectionClosed


connected_clients = set()
broadcast_lock = asyncio.Lock()


async def send_to_client(client, message):
    """Send a message to one client and discard closed connections."""
    try:
        await client.send(message)
    except ConnectionClosed:
        connected_clients.discard(client)


async def connection_handler(websocket):
    """Register a client and broadcast its messages."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            async with broadcast_lock:
                clients = tuple(connected_clients)
                await asyncio.gather(
                    *(
                        send_to_client(client, f"B:{message}")
                        for client in clients
                    )
                )
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the broadcast server."""
    async with websockets.serve(
        connection_handler, "127.0.0.1", 8765
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
