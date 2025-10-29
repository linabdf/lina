from flask import Flask, request, jsonify
from flask_cors import CORS # Nécessaire pour autoriser l'interaction depuis lina.html

app = Flask(__name__)
# Autorise le frontend (lina.html) à envoyer des requêtes au backend.
CORS(app)

# La route (l'adresse) que le frontend va appeler
@app.route('/api/interagir', methods=['POST'])
def interagir():
    # 1. Récupérer la donnée envoyée par le frontend
    data = request.json
    texte_recu = data.get('texte')

    # 2. Logique de traitement (simple vérification pour l'instant)
    if not texte_recu:
        # Envoie une réponse d'erreur
        return jsonify({"statut": "erreur", "message": "Aucun texte reçu."}), 400

    # 3. Afficher la donnée dans les logs du serveur (votre simulation de traitement)
    print(f"✅ Donnée reçue du Frontend: {texte_recu}")

    # 4. Répondre au frontend avec un message de succès
    return jsonify({
        "statut": "succes",
        "message": f"Backend a bien reçu et traité : '{texte_recu}'",
        "donnee_traitee": texte_recu.upper() # Exemple de traitement simple
    }), 200

# Le serveur écoute sur le port 5000 par défaut
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)