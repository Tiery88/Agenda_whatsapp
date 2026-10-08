from flask import Flask, request
import os, requests

app = Flask(__name__)
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "Tiery888")
WHATSAPP_TOKEN = os.environ.get("WHATSAPP_TOKEN")
PHONE_ID = os.environ.get("PHONE_NUMBER_ID")

@app.route("/")
def home(): return "Bot OK",200

@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge"),200
    return "Forbidden",403

@app.route("/webhook", methods=["POST"])
def hook():
    data = request.get_json()
    print(data)
    try:
        msg = data['entry'][0]['changes'][0]['value'].get('messages')
        if msg:
            from_num = msg[0]['from']
            text = msg[0]['text']['body']
            print(f"Message de {from_num}: {text}")
            # Répond
            url = f"https://graph.facebook.com/v20.0/{PHONE_ID}/messages"
            headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}"}
            payload = {"messaging_product":"whatsapp","to":from_num,"text":{"body": f"Bien reçu : '{text}' ✅ Je le note dans l'agenda."}}
            r = requests.post(url, headers=headers, json=payload)
            print(r.text)
    except Exception as e:
        print("Erreur:",e)
    return "OK",200
