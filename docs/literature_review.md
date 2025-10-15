Literature Review — SSL/TLS Vulnerabilities 

SSL/TLS secures web traffic by encrypting it and authenticating servers. Despite standards changes, typical misconfigurations continue to be frequently noted, and attackers can intercept or interfere with traffic.

Key issues:
- **Outdated protocol versions (SSLv3, TLS 1.0, TLS 1.1):** Older protocol versions have known issues and are no longer recommended. Servers that accept them are susceptible to a variety of downgrade and cryptographic attacks.
- **Weak cipher suites (RC4, EXPORT, NULL):** Some servers still accept weak ciphers which are subject to practical cryptanalysis or do not provide strong confidentiality or integrity.
- **Lack of forward secrecy:** If the website's encryption arrangement does not employ temporary (short-lived) keys for each session, anybody who obtains the server's private key in the future can unlock and read previously encrypted traffic.
- **Certificate problems (expired, missing intermediate, invalid issuer):** Expired or improperly chained certificates can break trust and allow browser warnings.
- **Missing security headers and features (Certificate Transparency):** These changes lower the danger of downgrades and spoofing, improve revocation checks, and make misissued certificates more visible.
- **Implementation vulnerabilities:** Problems like Heartbleed, POODLE, and ROBOT were serious bugs in how SSL/TLS was built or implemented. They allowed attackers to steal sensitive data or break the encryption on real websites.

For our project we will test sites for the above issues, document evidence, and map fixes to NIST/OWASP/IETF recommendations. This short review will be expanded in the final report with citations.
