# Utilise Nginx comme serveur web
FROM nginx:stable-alpine

# Copie ton index.html dans le dossier servi par Nginx
COPY index.html /usr/share/nginx/html/index.html

# Expose le port 80
EXPOSE 80

# Lancement de Nginx au premier plan
CMD ["nginx", "-g", "daemon off;"]
