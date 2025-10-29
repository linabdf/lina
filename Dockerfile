# Étape 1 : Utiliser une image de base Python
FROM python:3.11-slim

# Étape 2 : Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Étape 3 : Copier le fichier de dépendances et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape 4 : Copier l'application Backend (app.py) et le Frontend (lina.html)
COPY app.py .
COPY lina.html .

# Étape 5 : Exposer le port que Gunicorn va utiliser
# L'EXPOSE est désormais une simple documentation, la CMD gère le port réel ($PORT)
EXPOSE 8080

# Étape 6 : Commande de démarrage (CORRIGÉE)
# Utilise la variable d'environnement $PORT de Render
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]