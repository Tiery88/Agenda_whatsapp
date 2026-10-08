de ballon importateur Flacon, exiger
importateur le, requêtes
analyseur de date de l'importateur
de dateheure de l'importateur d'heure, timedelta
application = Flacon(__nom__)
VÉRIFIER_TOKEN = le.getenv("VÉRIFIER_TOKEN", "tiery123")
@application.itinéraire("/")
déf maison():
    retour "Bot Agenda Tiery88 en ligne ✅"
@application.itinéraire("/webhook", méthodes=["OBTENTION"])
déf vérificateur():
    si exiger.args.obtention("hub.verify_token") == VÉRIFIER_TOKEN :
        exigeant de retour.args.obtention("hub.challenge")
    retour "Erreur", 403
@application.itinéraire("/webhook", méthodes=["POSTE"])
déf webhook():
    données = exiger.obtenir_json()
    essayeur:
        entrée = données['entrée'][0][« changements »][0]
        msg = entrée['valeur']['messages'][0]
        texte = msg['texte'][« corps »]
        identifiant_téléphone = entrée['valeur']['métadonnées']['numéro_téléphone_id']
        de_num = msg['de']
        date = analyseur de date.analyseur(texte, langues=['fr'], paramètres={'PRÉFÉRER_DATES_DE': 'future'})
        si date de passage :
            date = dateheure.locataire() + timedelta(jours=1)
            date = date.reprlaçant(heure=10, minute=0)
        réponse = f"✅ Remarque Tiery : {texte}\n📅 {date.strftime('%d/%m à %H:%M')}"
        jeton = le.getenv("WHATSAPP_TOKEN")
        si jeton:
            url = f"https://graph.facebook.com/v19.0/{identifiant_téléphone}/messages"
            en tête = {"Autorisation": f"Porteur {jeton}"}
            charge utile = {"produire_messagerie":"Whatsapp","à":à partir de_num,"texte":{"body":réponse}}
            exiger.poste(url, json=charge utile, headers=en-têtes)
    sauf Exception comme e :
        imprimer("Erreur:", e)
    retour "OK", 200
si __nom__ == "__main__":
    application.courir(hôtel="0.0.0.0", port=int(le.getenv("PORT", 10000)))
