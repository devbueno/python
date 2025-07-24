import cv2
import asyncio
import websockets

# Define the WebSocket server address and port
HOST = '192.168.1.104'
PORT = 5000

async def send_frames(websocket, path):
    cap = cv2.VideoCapture(0)
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Encode frame as JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            data = buffer.tobytes()
            
            # Send data via WebSocket
            await websocket.send(data)

    finally:
        cap.release()

start_server = websockets.serve(send_frames, HOST, PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
