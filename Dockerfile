FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=admin
ENV MYSQL_DATABASE=colcalc
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=admin

EXPOSE 3306