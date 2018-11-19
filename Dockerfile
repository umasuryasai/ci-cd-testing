FROM centos
COPY sample.sh /
COPY test.sh /
CMD ["/sample.sh"]
