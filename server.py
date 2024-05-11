from flask import Flask, request

app = Flask(__name__)

@app.route('/send-key', methods=['POST'])
def receive_key():
    key = request.form['key']
    print("Received key from client:", key)
    return "Key received by server"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12340)