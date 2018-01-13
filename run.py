#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import http.server

# PORT = 8888
# server_address = ("", PORT)

# server = http.server.HTTPServer
# handler = http.server.CGIHTTPRequestHandler
# handler.cgi_directories = ["/"]
# print("Serveur actif sur le port :", PORT)

# httpd = server(server_address, handler)
# httpd.serve_forever()

# import asyncio
# import websockets

# direction = "Face"

# def setDir(string):
# 	global direction
# 	direction = string;

# async def mobile(websocket, path):
# 	while True:
# 		message = await websocket.recv()
# 		await consumer(message)


# async def computer(websocket, path):
# 	while True:
# 		message = await producer()
# 		await websocket.send(message)

# async def handler(websocket, path):
#     consumer_task = asyncio.ensure_future(consumer_handler(websocket))
#     producer_task = asyncio.ensure_future(producer_handler(websocket))
#     done, pending = await asyncio.wait(
#         [consumer_task, producer_task],
#         return_when=asyncio.FIRST_COMPLETED,
#     )

#     for task in pending:
#         task.cancel()
	

# start_server = websockets.serve(handler, 'localhost', 8765)

# # start_server_mobile = websockets.serve(mobile, 'localhost', 8765)
# # start_server = websockets.serve(computer, 'localhost', 8766)

# # asyncio.get_event_loop().run_until_complete(start_server_mobile)

# asyncio.get_event_loop().run_until_complete(start_server)

# asyncio.get_event_loop().run_forever()



LISTEN_ADDRESS = ('localhost', 8765)

import websockets
from server import client_handler
start_server = websockets.serve(client_handler, *LISTEN_ADDRESS)

import asyncio
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()