import requests
from flask import Flask, request

app = Flask(__name__)

ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN_HERE'

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    if request.args.get('hub.verify_token') == 'YOUR_VERIFY_TOKEN_HERE':
        return request.args.get('hub.challenge')
    return 'Verification token mismatch'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    # Handle received messages
    return "ok", 200

if __name__ == '__main__':
    app.run(port=5000)