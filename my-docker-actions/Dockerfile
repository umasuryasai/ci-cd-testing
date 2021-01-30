FROM alpine:3.2
RUN apk add --update nginx
COPY index.html /usr/share/nginx/html/index.html
COPY nginx.conf /etc/nginx/nginx.conf
CMD ["nginx", "-g", "daemon off;"]

# FROM httpd:2.4
# COPY ./my-docker-actions/index.html /usr/local/apache2/htdocs/index.html