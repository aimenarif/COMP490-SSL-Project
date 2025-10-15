# Methodology and Ethics

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
- Only test domains that are publicly accessible and do not require authorization such as school websites.
- Document the date/time of each scan and the user agent used.
- If a site owner requests removal of results or denies testing, immediately stop testing that domain and log the request.
- Include this ethics statement in the final report.

Contact & disclosure:
- To share a high-impact vulnerability, we will discreetly document the issue and contact the site administrator and let them knoe about a vulnerablity before making it public.
