import re

def analyze_pages(pages):
    findings = []

    # Strict email detection
    email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # STRONG phone number regex (India-optimized)
    phone_regex = r'(?:\+91[-\s]?|0)?[6-9]\d{9}'

    token_keywords = ["token", "secret", "api_key", "password", "passwd"]
    error_keywords = ["Exception", "Traceback", "Stack trace", "Fatal error"]

    for page in pages:
        url = page["url"]
        html = page["html"]

        # Email detection
        for e in re.findall(email_regex, html):
            findings.append({
                "url": url,
                "issue_type": "Email Address Exposed",
                "pattern": e,
                "severity": "Medium"
            })

        # Phone detection (strict)
        for p in re.findall(phone_regex, html):
            findings.append({
                "url": url,
                "issue_type": "Phone Number Exposed",
                "pattern": p,
                "severity": "Medium"
            })

        # Possible credentials
        for key in token_keywords:
            if key.lower() in html.lower():
                findings.append({
                    "url": url,
                    "issue_type": "Potential Credential Exposure",
                    "pattern": key,
                    "severity": "High"
                })

        # Error pages
        for err in error_keywords:
            if err.lower() in html.lower():
                findings.append({
                    "url": url,
                    "issue_type": "Stack Trace / Error Message Found",
                    "pattern": err,
                    "severity": "High"
                })

        # Public admin pages
        if any(admin in url.lower() for admin in ["admin", "debug", "config"]):
            findings.append({
                "url": url,
                "issue_type": "Suspicious Public Admin Page",
                "pattern": url,
                "severity": "High"
            })

    return findings
