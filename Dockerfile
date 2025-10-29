#serveur web speed
FROM nginx:stable-alpine
#copy the
COPY lina.html /usr/share/nginx/html/index.html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
