const dgram = require('dgram');
const WebSocket = require('ws');
const pickle = require('pickle');

const udpServer = dgram.createSocket('udp4');
const wss = new WebSocket.Server({ port: 8081 });

udpServer.on('message', (message, remote) => {
    // Get the frame size
    const frameSize = message.readUInt32LE(0);
    const frameData = message.slice(4, 4 + frameSize);

    // Deserialize the frame
    const frame = pickle.loads(frameData);

    // Broadcast to all connected WebSocket clients
    wss.clients.forEach(client => {
        if (client.readyState === WebSocket.OPEN) {
            client.send(frameData);
        }
    });
});

udpServer.bind(8082);  // Listening for UDP on port 8082
