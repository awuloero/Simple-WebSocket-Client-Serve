
# Simple WebSocket Client-Server

This repository contains a basic implementation of a WebSocket client and server using Python's `asyncio` and `websockets` libraries.

## Overview

The project consists of two main scripts:

- `client.py`: A WebSocket client that connects to the server, sends user-input messages, and prints responses from the server.
- `server.py`: A WebSocket server that listens for client connections, prints received messages, and responds to the client.

## Requirements

- Python 3.7+
- `websockets` library

You can install the required library using pip:

```sh
pip install websockets
```

## Usage

### Running the Server

1. Ensure you have Python 3.7 or higher installed.
2. Install the `websockets` library if you haven't already.
3. Run the server script:

```sh
python server.py
```

The server will start and listen for connections on `ws://localhost:5000`.

### Running the Client

1. Ensure the server is running.
2. Run the client script:

```sh
python client.py
```

3. Enter messages when prompted. The messages will be sent to the server, and you will see the server's response.
4. To exit the client, type `exit`.

## How It Works

- The server script initializes a WebSocket server that listens on `localhost:5000`.
- When a client connects, the server can receive messages and send responses.
- The client script connects to the server, sends user-input messages, and prints the server's responses.

## Example

### Server Output

```sh
Received message from client: Hello, Server!
Received message from client: How are you?
```

### Client Output

```sh
connection successful!!!
Enter a message to send to the server: Hello, Server!
from server: Hello, Client! You said: Hello, Server!
Enter a message to send to the server: How are you?
from server: Hello, Client! You said: How are you?
```
