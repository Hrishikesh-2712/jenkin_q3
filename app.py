from flask import Flask
import socket
app = Flask(__name__)

@app.route("/")
def index():
    hostname = socket.gethostname()
    return "Hello from "+hostname

app.run(host="0.0.0.0", port="5000")
