# Secure_client.py
import asyncio
import websockets
import pathlib
import ssl

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
ssl_context.load_verify_locations(localhost_pem)

async def hello():
    async with websockets.connect("wss://localhost:5000", ssl=ssl_context) as websocket:
        print('connection successful!!!')
        while True:
            msg = input("Enter a message to send to the server: ")
            if (msg=="exit"):
                return;
            else:
                await websocket.send(msg)
                response = await websocket.recv()
                print(f"from server: {response}")
      
asyncio.get_event_loop().run_until_complete(hello())
