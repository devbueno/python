import cv2
import socket
import struct
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# IP and Port of the middle server
MID_SERVER_IP = '18.231.27.147'
MID_SERVER_PORT = 5002

# Define maximum packet size (slightly reduced to accommodate the header)
MAX_PACKET_SIZE = 65507 - 4  # 65507 is the max UDP size, 4 bytes for the header

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open the camera
cap = cv2.VideoCapture(0)

logging.info("Starting camera capture")

while True:
    ret, frame = cap.read()
    if not ret:
        logging.error("Failed to read frame from camera")
        break

    # Encode frame as JPEG
    _, buffer = cv2.imencode('.jpg', frame)
    data = buffer.tobytes()
    
    # Split data into chunks
    num_chunks = (len(data) + MAX_PACKET_SIZE - 1) // MAX_PACKET_SIZE
    for i in range(num_chunks):
        chunk = data[i*MAX_PACKET_SIZE:(i+1)*MAX_PACKET_SIZE]
        header = struct.pack("H", i) + struct.pack("H", num_chunks)  # chunk index and total number of chunks
        sock.sendto(header + chunk, (MID_SERVER_IP, MID_SERVER_PORT))
        logging.debug(f"Sent chunk {i+1}/{num_chunks}")

cap.release()
sock.close()
logging.info("Camera capture stopped")
