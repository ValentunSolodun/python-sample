import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
    while True:
        await websocket.send('Web Socket works')
        await asyncio.sleep(5)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()