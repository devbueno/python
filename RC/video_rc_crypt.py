import cv2
from flask import Flask, Response
import ssl
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import numpy as np

app = Flask(__name__)
camera = cv2.VideoCapture(0)

# Encryption settings
key = b'YOUR_KEY_16_BYTES'
iv = b'YOUR_IV_16_BYTES'
cipher = AES.new(key, AES.MODE_CBC, iv)

def encrypt_frame(frame):
    # Convert frame to bytes
    frame_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
    
    # Pad the frame to be a multiple of 16 bytes
    padded_frame = pad(frame_bytes, AES.block_size)
    
    # Encrypt the padded frame
    encrypted_frame = cipher.encrypt(padded_frame)
    
    # Encode the encrypted frame as base64
    encrypted_frame_b64 = base64.b64encode(encrypted_frame)
    
    return encrypted_frame_b64

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            encrypted_frame = encrypt_frame(frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + encrypted_frame + b'\r\n')

@app.route('/')
def index():
    return '<html><body><img src="/video_feed"></body></html>'

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('server.crt', 'server.key')
    app.run(host='192.168.1.104', debug=True, ssl_context=context)
