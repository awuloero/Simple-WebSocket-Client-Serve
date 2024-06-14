# secure_server.py
import asyncio
import websockets
import pathlib
import ssl

async def server(websocket, path):
    async for message in websocket:
        print(f"Received message from client: {message}")
        await websocket.send(f"Hello, Client! You said: {message}")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
ssl_context.load_cert_chain(localhost_pem)

start_server = websockets.serve(server, "localhost", 5000, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()