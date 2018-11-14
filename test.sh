#!/bin/bash
cat index.html > /usr/share/httpd/noindex/index.html
systemctl restart httpd
