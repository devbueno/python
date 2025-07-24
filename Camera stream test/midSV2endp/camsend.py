import cv2
import socket
import pickle
import struct

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP and Port to send the frames
ip = '10.1.1.1'
port = 8081

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Serialize frame
    data = pickle.dumps(frame)
    
    # Send frame length first
    message_size = struct.pack("L", len(data))

    # Send data via UDP
    sock.sendto(message_size + data, (ip, port))

cap.release()
sock.close()
