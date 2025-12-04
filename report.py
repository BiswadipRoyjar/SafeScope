from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def generate_pdf(url, pages, findings, scan_id):
    directory = "pdf_reports"
    os.makedirs(directory, exist_ok=True)

    pdf_path = f"{directory}/scan_{scan_id}.pdf"

    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, height - 50, f"Scan Report: {url}")

    c.setFont("Helvetica", 12)
    y = height - 90

    c.drawString(30, y, f"Total Pages Scanned: {len(pages)}")
    y -= 20
    c.drawString(30, y, f"Total Issues Found: {len(findings)}")
    y -= 30

    for f in findings:
        if y < 100:
            c.showPage()
            y = height - 50

        c.drawString(30, y, f"- {f['issue_type']} (Severity: {f['severity']})")
        y -= 15
        c.drawString(50, y, f"URL: {f['url']}")
        y -= 15
        c.drawString(50, y, f"Found: {f['pattern']}")
        y -= 25

    c.save()
    return pdf_path
