# client.py
import asyncio
import websockets


async def hello():
    async with websockets.connect("ws://localhost:5000") as websocket:
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