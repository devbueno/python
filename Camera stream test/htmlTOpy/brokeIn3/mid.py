import asyncio
import websockets
import socket
import struct
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Define the WebSocket server address and port
WS_HOST = '192.168.1.104'
WS_PORT = 5001

# Create a UDP socket
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_sock.bind(('192.168.1.104', 5002))

# Buffer to store incoming chunks
chunks_buffer = {}

async def forward_frames(websocket, path):
    logging.info("WebSocket client connected")
    try:
        while True:
            # Receive data from the Camera Capture Server
            message, addr = udp_sock.recvfrom(65507)  # Max UDP size
            
            # Extract the header
            chunk_index, num_chunks = struct.unpack("HH", message[:4])
            chunk_data = message[4:]
            
            # Reassemble the chunks
            if addr not in chunks_buffer:
                chunks_buffer[addr] = [None] * num_chunks
            
            chunks_buffer[addr][chunk_index] = chunk_data
            
            # Check if we have all chunks
            if all(chunk is not None for chunk in chunks_buffer[addr]):
                frame_data = b''.join(chunks_buffer[addr])
                del chunks_buffer[addr]
                
                # Forward the frame data to WebSocket clients
                await websocket.send(frame_data)
                logging.info("Frame forwarded to WebSocket client")
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        logging.info("WebSocket client disconnected")

start_server = websockets.serve(forward_frames, WS_HOST, WS_PORT)

logging.info(f"Starting WebSocket server on ws://{WS_HOST}:{WS_PORT}")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
