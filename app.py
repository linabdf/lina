from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS # Nécessaire pour autoriser l'interaction depuis lina.html

app = Flask(__name__)
# Autorise le frontend (lina.html) à envoyer des requêtes au backend.
CORS(app)

# --- ROUTE 1 : Servir la page d'accueil (Correction de l'erreur 404) ---
# Lorsque l'utilisateur va sur l'URL principale (/)
@app.route('/')
def index():
    # Cherche le fichier 'lina.html' dans le sous-dossier 'static'
    # ATTENTION: Assurez-vous que lina.html est bien dans le dossier 'static/'
    return send_from_directory('.', 'lina.html')



# --- ROUTE 2 : API d'interaction ---
@app.route('/api/interagir', methods=['POST'])
def interagir():
    # 1. Récupérer la donnée envoyée par le frontend
    data = request.json
    texte_recu = data.get('texte')

    if not texte_recu:
        return jsonify({"statut": "erreur", "message": "Aucun texte reçu."}), 400

    # 2. Logique de traitement (simulation)
    print(f"✅ Donnée reçue du Frontend: {texte_recu}")

    # 3. Répondre au frontend
    return jsonify({
        "statut": "succes",
        "message": f"Backend a bien reçu et traité : '{texte_recu}' (Version simple et stable)",
        "donnee_traitee": texte_recu.upper()
    }), 200

# Ce bloc n'est utilisé que pour les tests en local
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)