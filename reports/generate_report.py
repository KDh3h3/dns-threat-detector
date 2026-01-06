from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf_report(findings):
    c = canvas.Canvas("reports/DNS_Threat_Report.pdf", pagesize=A4)
    text = c.beginText(40, 800)

    text.textLine("DNS Threat Detection Report")
    text.textLine("")
    text.textLine("Executive Summary:")
    text.textLine("Suspicious DNS behavior detected indicating possible malware activity.")
    text.textLine("")

    text.textLine("Findings:")
    for key, value in findings.items():
        text.textLine(f"- {key}: {value}")

    text.textLine("")
    text.textLine("Recommendations:")
    text.textLine("- Investigate affected internal hosts")
    text.textLine("- Block malicious domains")
    text.textLine("- Enable continuous DNS monitoring")

    c.drawText(text)
    c.save()
