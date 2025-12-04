SafeScope – AI-Inspired Web Exposure Scanner (FastAPI + Python)

A lightweight, fast, and intelligent web exposure scanner that crawls a domain, detects sensitive data leaks, generates PDF reports, and shows real-time scan progress in a hacker-style green UI.

🔥 Why I Built SafeScope

SafeScope is a full-stack cybersecurity automation tool that demonstrates strong skills in:

Python backend development

Web crawling & parsing

FastAPI orchestration

Security exposure detection

PDF report generation

Real-time UI updates

System design

Error handling

Cybersecurity principles

It is fully open-source and built for learning, exploring security automation, and demonstrating backend engineering capabilities.

🚀 Features
✔ Deep Web Crawler

Crawls internal links up to configurable depth

Skips files (PDFs, images, videos)

Avoids loops, login/logout traps

Extracts HTML from every page

✔ Exposure Detection Engine

Detects security issues across all pages:

🔴 High Severity

Exposed credentials (password, token, api_key, secret)

Public admin/config/debug pages

Error stack traces

🟡 Medium Severity

Valid phone numbers (strict regex)

Email address leaks

🟢 Low Severity

Informational notes

✔ Real-Time Scan Status Page

Live progress bar

Current URL being scanned

Pages scanned count

Auto-redirect to results

✔ PDF Report Generation

Every scan creates a detailed PDF with:

Target URL

Findings

Severity levels

Exact URLs where issues were found

Timestamp

Downloadable from the dashboard.

✔ Hacker-Themed Green UI

Neon-green terminal look

Severity colors:

High = Red

Medium = Yellow

Low = Green

Animated progress bar

Clean FastAPI/Jinja2 frontend

🧪 Screenshots (Add After Upload)

Add screenshots in this format:

![Screenshot](assets/home.png)
![Scan Status](assets/status.png)
![Results](assets/results.png)

🏗️ Tech Stack
Backend

Python 3.x

FastAPI

Requests

BeautifulSoup

ReportLab (PDF generation)

Frontend

HTML / Jinja2 Templates

JavaScript (live polling)

Hacker-theme UI CSS

Other Tools

UVicorn

Git

Virtual Environment

⚙️ Installation
git clone https://github.com/<your-username>/SafeScope-Web-Exposure-Scanner.git
cd SafeScope-Web-Exposure-Scanner

pip install -r requirements.txt


Run the server:

uvicorn app.main:app --reload


Open in browser:

http://127.0.0.1:8000

🛠️ Project Structure
/app
    main.py
    crawler.py
    analyzer.py
    report.py
    templates/
        base.html
        home.html
        status.html
        result.html

/pdf_reports

requirements.txt
README.md

📌 How It Works (Architecture)
1️⃣ User enters a website URL
2️⃣ Background task starts scanning
3️⃣ Crawler explores all internal links
4️⃣ Analyzer extracts exposures using regex rules
5️⃣ Status page shows real-time scan updates
6️⃣ PDF report is generated
7️⃣ Results + Download link shown to user
🔮 Future Enhancements

Planned improvements:

AI-powered explanation for each finding

XSS detection

SQL Injection detection

CORS misconfiguration audit

JWT token scanner

JS file security scanner

Docker deployment

Websocket live updates

Auth system & user accounts

Dashboard with historical scans

🤝 Contributing

If you want to extend the project with more vulnerability checks or better UI, feel free to submit a PR or open issues.

📄 License

MIT License – free for personal and commercial use.

💬 Contact

If you’re interested in:

Python backend development

Cybersecurity automation

AI/ML engineering

Networking, API testing, automation

Let’s connect!

LinkedIn: https://linkedin.com/in/your-profile

GitHub: https://github.com/your-username
