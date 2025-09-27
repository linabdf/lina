FROM nginx:stable-alpine
COPY lina.html /usr/share/nginx/html/index.html
COPY favicon.ico /usr/share/nginx/html/favicon.ico
COPY css/ /usr/share/nginx/html/css/
COPY js/ /usr/share/nginx/html/js/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
