from flask import Flask, jsonify, render_template
import socket


app = Flask(__name__)

# Function to fetch hostname and ip
def fetchDetails():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return str(hostname), str(ip)

@app.route('/')
def hello_world():
    return 'minha namorada é linda, mulher da minha vida!'

@app.route('/health')
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    hostname, ip = fetchDetails()
    return render_template('index.html',HOSTNAME=hostname, IP=ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
