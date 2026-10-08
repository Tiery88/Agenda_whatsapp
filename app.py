from flask import Flask, request
import os, requests, json

app = Flask(__name__)

@app.route("/")
def home():
    return "OK", 200

@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == os.getenv("VERIFY_TOKEN"):
        return request.args.get("hub.challenge"), 200
    return "bad token", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("DATA:", json.dumps(data))
    try:
        entry = data['entry'][0]['changes'][0]['value']
        if 'messages' in entry:
            msg = entry['messages'][0]
            from_id = msg['from']
            txt = msg['text']['body']
            print(f"RECU de {from_id}: {txt}")

            # Répondre
            token = os.getenv("WHATSAPP_TOKEN")
            phone_id = os.getenv("PHONE_NUMBER_ID")
            url = f"https://graph.facebook.com/v20.0/{phone_id}/messages"
            payload = {
                "messaging_product": "whatsapp",
                "to": from_id,
                "text": {"body": f"Reçu ✅ : {txt}"}
            }
            headers = {"Authorization": f"Bearer {token}", "Content-Type":"application/json"}
            r = requests.post(url, json=payload, headers=headers)
            print("ENVOI:", r.text)
    except Exception as e:
        print("Erreur:", e)
    return "OK", 200
