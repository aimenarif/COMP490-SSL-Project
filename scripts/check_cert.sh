#!/usr/bin/env bash

if [[ -z "$1" ]]; then
    echo "Usage: $0 <hostname>"
    exit 1
fi

host="$1"

echo | openssl s_client \
    -servername "$host" \
    -connect "$host:443" 2>/dev/null \
    | openssl x509 -noout -text
