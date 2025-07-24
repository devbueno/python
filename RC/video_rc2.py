from flask import Flask, Response

app = Flask(__name__)

# Define route handler for the root URL
@app.route('/')
def index():
    return 'Webcam Stream Server'

# Define route handler for favicon.ico
@app.route('/favicon.ico')
def favicon():
    return ''

# Your existing video feed route handler
@app.route('/video_feed')
def video_feed():
    # Your video streaming logic here
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)