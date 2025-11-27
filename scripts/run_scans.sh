#!/usr/bin/env bash
set -euo pipefail

# Get the absolute path to the folder where the script lives
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

SCANS_DIR="$PROJECT_ROOT/scans"
TARGETS_FILE="$PROJECT_ROOT/targets.txt"

# Make sure subfolders exist
mkdir -p "$SCANS_DIR/sslyze" "$SCANS_DIR/nmap"

# Read all hosts from targets.txt
HOSTS=()
while read -r host; do
    [[ -z "$host" ]] && continue
    HOSTS+=("$host")
done < "$TARGETS_FILE"

# Prepare SSLyze target list with port 443
SSL_TARGETS=()
for host in "${HOSTS[@]}"; do
    SSL_TARGETS+=("${host}:443")
done

echo "=== Running SSLyze scan for all hosts ==="
# Run SSLyze on all targets at once
sslyze --json_out="$SCANS_DIR/sslyze/all_hosts.json" "${SSL_TARGETS[@]}" || echo "SSLyze scan failed"

echo "=== Running Nmap scan for each host ==="
for host in "${HOSTS[@]}"; do
    echo "--- Scanning $host with Nmap ---"
    nmap --script ssl-enum-ciphers -p 443 \
        -oN "$SCANS_DIR/nmap/${host}_nmap.txt" \
        "$host"
    sleep 2
done

echo "=== All scans completed ==="
