#!/bin/sh

set -ex

# Start SSH server.
export HOME=/root

if test ! -z "$PUBKEY"; then
    echo "$PUBKEY" >> /root/.ssh/authorized_keys
fi

/usr/sbin/sshd -D -h /etc/ssh/ssh_host_ecdsa_key -p 2222
