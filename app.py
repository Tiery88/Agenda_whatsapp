from flask import Flask, request
import os
print("Démarrage serveur...")

app = Flask(__name__)
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "Tiery888")

@app.route("/")
def home():
    return "Serveur Agenda OK", 200

@app.route("/webhook", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    print(f"Facebook demande verif -> token recu: {token}")
    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("VERIFICATION OK")
        return challenge, 200
    else:
        print(f"VERIFICATION REFUSEE - Attendu: {VERIFY_TOKEN}")
        return "Forbidden", 403

@app.route("/webhook", methods=["POST"])
def receive_message():
    print("POST /webhook RECU !")
    print(request.get_json())
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
