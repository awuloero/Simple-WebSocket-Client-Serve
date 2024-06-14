# Simple WebSocket Client-Server

This repository contains basic implementations of both a secure and non-secure WebSocket client and server using Python's `asyncio` and `websockets` libraries.

## Overview

The project consists of four main scripts:

- `client.py`: A non-secure WebSocket client that connects to the server, sends user-input messages, and prints responses from the server.
- `server.py`: A non-secure WebSocket server that listens for client connections, prints received messages, and responds to the client.
- `secure_client.py`: A secure WebSocket client that uses SSL/TLS to connect to the server, sends user-input messages, and prints responses from the server.
- `secure_server.py`: A secure WebSocket server that uses SSL/TLS, listens for client connections, prints received messages, and responds to the client.

## Requirements

- Python 3.7+
- `websockets` library

You can install the required library using pip:

```sh
pip install websockets
```

## Usage

### Running the Non-Secure Server

1. Ensure you have Python 3.7 or higher installed.
2. Install the `websockets` library if you haven't already.
3. Run the server script:

```sh
python server.py
```

The server will start and listen for connections on `ws://localhost:5000`.

### Running the Non-Secure Client

1. Ensure the server is running.
2. Run the client script:

```sh
python client.py
```

3. Enter messages when prompted. The messages will be sent to the server, and you will see the server's response.
4. To exit the client, type `exit`.

### Running the Secure Server

1. Ensure you have Python 3.7 or higher installed.
2. Install the `websockets` library if you haven't already.
3. Ensure you have `localhost.pem` in the same directory as the scripts.
4. Run the secure server script:

```sh
python secure_server.py
```

The server will start and listen for connections on `wss://localhost:5000`.

### Running the Secure Client

1. Ensure the secure server is running.
2. Run the secure client script:

```sh
python secure_client.py
```

3. Enter messages when prompted. The messages will be sent to the server, and you will see the server's response.
4. To exit the client, type `exit`.

## How It Works

- The non-secure scripts (`server.py` and `client.py`) initialize a WebSocket server and client that communicate over an unencrypted connection on `localhost:5000`.
- The secure scripts (`secure_server.py` and `secure_client.py`) initialize a WebSocket server and client that communicate over an encrypted connection using SSL/TLS on `localhost:5000`.

## Example

### Non-Secure Server Output

```sh
Received message from client: Hello, Server!
Received message from client: How are you?
```

### Non-Secure Client Output

```sh
connection successful!!!
Enter a message to send to the server: Hello, Server!
from server: Hello, Client! You said: Hello, Server!
Enter a message to send to the server: How are you?
from server: Hello, Client! You said: How are you?
```

### Secure Server Output

```sh
Received message from client: Hello, Secure Server!
Received message from client: How are you, securely?
```

### Secure Client Output

```sh
connection successful!!!
Enter a message to send to the server: Hello, Secure Server!
from server: Hello, Client! You said: Hello, Secure Server!
Enter a message to send to the server: How are you, securely?
from server: Hello, Client! You said: How are you, securely?
```
