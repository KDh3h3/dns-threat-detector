import pandas as pd

from detectors.entropy_detector import detect_high_entropy
from detectors.nxdomain_detector import detect_nxdomain_abuse
from detectors.beaconing_detector import detect_beaconing
from detectors.volume_detector import detect_volume_spikes

from ai.ai_detector import run_ai_detection
from dashboard.dashboard import run_dashboard
from reports.generate_report import generate_pdf_report
from utils.helpers import risk_score

CSV_PATH = "data/dns_logs.csv"

df = pd.read_csv(CSV_PATH)
logs = df.to_dict(orient="records")

domains = df["query"].tolist()

entropy_hits = detect_high_entropy(domains)
nxdomain_hits = detect_nxdomain_abuse(logs)
beaconing_hits = detect_beaconing(logs)
volume_hits = detect_volume_spikes(logs)

ai_anomalies = run_ai_detection(CSV_PATH)

score = risk_score(entropy_hits, nxdomain_hits, volume_hits)

findings = {
    "High Entropy Domains": len(entropy_hits),
    "NXDOMAIN Abuse": nxdomain_hits,
    "Beaconing Domains": beaconing_hits,
    "Volume Spikes": volume_hits,
    "AI Anomalies Detected": len(ai_anomalies),
    "Overall Risk Score": score
}

print("=== DNS Threat Findings ===")
print(findings)

run_dashboard(CSV_PATH)
generate_pdf_report(findings)
