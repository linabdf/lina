# Étape 1 : Utiliser une image de base Python
FROM python:3.11-slim

# Étape 2 : Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Étape 3 : Copier le fichier de dépendances et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape 4 : Copier l'application Backend (app.py) et le Frontend (lina.html)
# Nous copions lina.html ici car nous allons le servir avec Flask si besoin,
# ou le laisser à la racine si nous utilisons un autre serveur (Nginx) plus tard.
COPY app.py .
COPY lina.html .

# Étape 5 : Exposer le port que Gunicorn va utiliser
# Render utilisera cette variable d'environnement pour configurer le port
EXPOSE 8080

# Étape 6 : Commande de démarrage
# Utiliser Gunicorn pour lancer l'application Flask en production
# '-b 0.0.0.0:$PORT' indique d'écouter sur le port donné par l'environnement Render
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]