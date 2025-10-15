Methodology and Ethics

Scope:
- Only publicly available HTTPS endpoints specified in targets/targets.txt are subject to testing.
- No non-public resources, internal IP ranges, or authenticated endpoints will be evaluated.
- No active exploitation or brute force strategies will be used that might interfere with services.
Tools (examples):
- SSLyze (automated TLS checks)
- OpenSSL (manual certificate inspection)
- nmap with ssl-enum-ciphers (cross-check cipher lists)
- curl (header checks)

Method of testing:
1. Perform non-aggressive scans (no brute force attacks) once for each domain.
2. Take atleast a 10 second break in between scans to prevent rate-limiting.
3. Save all raw outputs with timestamps to outputs/.
4. Before reporting, manually check for any serious or high issues using curl and OpenSSL.

Ethics and permissions:
We will following ethical cybersecurity practices
- Only test domains that are publicly accessible and do not require authorization such as school websites.
- Document the date/time of each scan and the user agent used.
- If a site owner requests removal of results or denies testing, immediately stop testing that domain and log the request.
- Only technical details (protocols, cipher names, expiry dates) will be kept. More details might be kept for educational or demonstrational purposes only
- No personal or private data will be collected.
- Files will be named with timestamps for transparency.
- We will not bypass authentication 

Step-by-Step method:
1. First, we will select a domain to test, for example, www.ufv.ca.
2. Then we will run a SSLyze scan using regular scan mode such as sslyze --regular www.ufv.ca.
3. We might get something like outputs/ufv_scan_2025-10-14.txt.
4. Cross check results using `nmap` or `openssl` if SSLyze finds a potential problem.
5. Inspect headers with `curl -I https://domain.com` to check for HSTS and redirection.
6. Then we record the headings like (TLS version, weak ciphers, certificate expiry, etc.) in `docs/results_summary.csv` or such
7. Some things to look for while doing running our scans:
    - **Old TLS versions** like TLS 1.0 or 1.1  
    - **Weak ciphers** such as RC4, 3DES, or NULL ciphers  
    - **Expired or invalid certificates**  
    - **Missing security features** such as: HSTS header, OCSP stapling, Forward secrecy support  
    - **Proper certificate chain** (trusted by browsers)
       
Contact & disclosure:
If we ever find a serious issue (like an expired certificate or outdated TLS version):
1. We will double-check the result with another tool.  
2. We will write a short description of the issue.  
3. We will contact the site’s technical or security email to inform them politely about a vulnerability.  
4. We will not share or publish sensitive details publicly.
5. We will make sure to provide full reports or evidences found incase of a vulnerability.
By following the guidelines and ethics discussed above, we can study SSL/TLS configurations responsibly and produce meaningful results.
