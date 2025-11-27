#!/usr/bin/env bash

if [[ -z "$1" ]]; then
    echo "Usage: $0 <hostname>"
    exit 1
fi

host="$1"

curl -I "https://$host" 2>/dev/null | grep -i strict-transport-security \
    || echo "HSTS not enabled"
