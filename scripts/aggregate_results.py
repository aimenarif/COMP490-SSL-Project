import glob, csv, os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SCANS_DIR = os.path.join(PROJECT_ROOT, 'scans')
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
OUTPUT_CSV = os.path.join(DATA_DIR, 'summary.csv')
os.makedirs(DATA_DIR, exist_ok=True)

hosts = set()
hosts.update(os.path.basename(f).split('_')[0] for f in glob.glob(os.path.join(SCANS_DIR, 'nmap', '*_nmap.txt')))

output_rows = []

for host in hosts:
    # TLS versions
    tls_versions = set()
    nmap_file = os.path.join(SCANS_DIR, 'nmap', f'{host}_nmap.txt')
    if os.path.exists(nmap_file):
        with open(nmap_file) as f:
            data = f.read().lower()
            if "tlsv1.3" in data: tls_versions.add("TLS 1.3")
            if "tlsv1.2" in data: tls_versions.add("TLS 1.2")
            if "tlsv1.1" in data: tls_versions.add("TLS 1.1")
            if "tlsv1.0" in data: tls_versions.add("TLS 1.0")

    # Weak ciphers / PFS
    weak_ciphers = set()
    pfs = False
    if any(x in data for x in ["export", "rc4", "3des", "null"]):
        weak_ciphers.add("weak cipher detected")
    if "ecdhe" in data or "dhe" in data:
        pfs = True

    # HSTS
    hsts_file = os.path.join(SCANS_DIR, 'hsts', f'{host}_hsts.txt')
    hsts = False
    if os.path.exists(hsts_file):
        with open(hsts_file) as f:
            if "strict-transport-security" in f.read().lower():
                hsts = True

    # Cert issues
    cert_file = os.path.join(SCANS_DIR, 'certs', f'{host}_cert.txt')
    cert_issues = []
    if os.path.exists(cert_file):
        with open(cert_file) as f:
            cert_data = f.read().lower()
            if any(x in cert_data for x in ["expired", "self-signed", "hostname mismatch"]):
                cert_issues.append("certificate issue")

    output_rows.append({
        "host": host,
        "tls_versions": "; ".join(tls_versions) or "unknown",
        "weak_ciphers": "; ".join(weak_ciphers) or "none",
        "pfs": pfs,
        "hsts": hsts,
        "cert_issues": "; ".join(cert_issues) or "none"
    })

# Write CSV
with open(OUTPUT_CSV, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["host","tls_versions","weak_ciphers","pfs","hsts","cert_issues"])
    writer.writeheader()
    writer.writerows(output_rows)

print(f"Created summary file at: {OUTPUT_CSV}")
