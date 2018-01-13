import asyncio
import pxssh

# The set of clients connected to this server. It is used to distribute
# messages.
clients = {} #: {websocket: name}

@asyncio.coroutine
def client_handler(websocket, path):

    # The first line from the client is the name
    name = yield from websocket.recv()
    clients[websocket] = name

    # Handle messages from this client
    while True:
        message = yield from websocket.recv()
        if message is None:
            their_name = clients[websocket]
            del clients[websocket]
            print('Client closed connection', websocket)
            break

        # Send message to all clients
        for client, _ in clients.items():
            print(message)
            yield from client.send('{}'.format(message))
