from flask import Flask, request
import os
import dateparser
from datetime import datetime

app = Flask(__name__)

VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "tiery123")

@app.route("/", methods=["GET"])
def home():
    return "Bot WhatsApp Agenda OK", 200

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == VERIFY_TOKEN:
            return challenge, 200
        return "Token invalide", 403
    
    if request.method == "POST":
        data = request.get_json()
        print(data)
        # Ici on traitera les messages
        return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
