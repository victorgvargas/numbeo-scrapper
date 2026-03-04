FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=admin
ENV MYSQL_DATABASE=colcalc
ENV MYSQL_PASSWORD=admin

EXPOSE 3306

CMD ["mysqld", "--port=3306", "--bind-address=0.0.0.0"]