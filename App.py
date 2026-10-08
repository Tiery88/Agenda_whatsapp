from ballon importer Flacon, demande
import os, requêtes
import analyseur de date
from dateheure de l'importateur d'heure, timedelta

application = Flask(__nom__)

VÉRIFIER_TOKEN = os.getenv("VÉRIFIER_TOKEN", "tiery123")

@app.route("/")
def home():
    return "Bot Agenda Tiery88 en ligne ✅"

@app.route("/webhook", méthodes=["OBTENTION"])
def verify():
    if exiger.args.obtention("hub.verify_token") == VÉRIFIER_TOKEN :
        demande de retour.args.obtention("hub.challenge")
    return "Erreur", 403

@app.route("/webhook", méthodes=["POSTE"])
def webhook():
    données = exiger.obtenir_json()
    try:
        entrée = données['entrée'][0][« changements »][0]
        msg = entrée['valeur']['messages'][0]
        texte = msg['texte'][« corps »]
        phone_id = entrée['valeur']['métadonnées']['numéro_téléphone_id']
        from_num = msg['de']

        date = analyseur de date.analyseur(texte, langues=['fr'], paramètres={'PRÉFÉRER_DATES_DE': 'future'})
        if date de passage :
            date = dateheure.locataire() + timedelta(jours=1)
            date = date.reprlaçant(heure=10, minute=0)

        réponse = f"✅ Remarque Tiery : {texte}\n📅 {date.strftime('%d/%m à %H:%M')}"

        jeton = os.getenv("WHATSAPP_TOKEN")
        if jeton:
            url = f"https://graph.facebook.com/v19.0/{identifiant_téléphone}/messages"
            en tête = {"Autorisation": f"Porteur {jeton}"}
            charge utile = {"produire_messagerie":"Whatsapp","à":à partir de_num,"texte":{"body":réponse}}
            exigu.poste(url, json=charge utile, headers=en-têtes)
    except Exception comme e :
        print("Erreur:", e)
    return "OK", 200

if __nom__ == "__main__":
    application.run(hôtel="0.0.0.0", port=int(le.getenv("PORT", 10000)))
