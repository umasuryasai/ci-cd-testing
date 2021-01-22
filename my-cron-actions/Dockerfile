FROM centos:latest
WORKDIR /
RUN yum -y update && yum -y install crontabs java
ADD crontab /etc/cron.d/cron_test
ADD cron.sh .
ADD springboot_employee-0.0.1-8080.jar employee.jar
RUN chmod 0644 /etc/cron.d/cron_test
RUN touch /var/log/cron.log
RUN crontab /etc/cron.d/cron_test
CMD crond && nohup java -jar /employee.jar