FROM httpd:2.4
WORKDIR /ci-cd-testing/others
RUN ls -al
COPY ./index.html /usr/local/apache2/htdocs/index.html
# RUN service httpd restart