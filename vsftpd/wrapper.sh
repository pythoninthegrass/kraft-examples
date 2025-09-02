#!/usr/bin/env bash

set -e

mkdir -p /home/ftpuser && \
    echo "Hello from UKP!" > /home/ftpuser/hello.txt
chown -R ftpuser:ftpuser /home/ftpuser

/usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf &

tail -f /var/log/vsftpd.log
