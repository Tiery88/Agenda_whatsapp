from flask import Flask, request
import os

app = Flask(__name__)

VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "Tiery888")

@app.route("/", methods=["GET"])
def home():
    return "OK - Agenda WhatsApp est en ligne", 200

@app.route("/webhook", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    print(f"Verification demandée, token reçu: {token}")
    if token == VERIFY_TOKEN:
        print("Token OK !")
        return challenge, 200
    else:
        print(f"Token REFUSE, attendu: {VERIFY_TOKEN}")
        return "Token invalide", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("POST /webhook reçu:", data)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
