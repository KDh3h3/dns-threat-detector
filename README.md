# DNS Threat Detector  
**Early-Stage Threat Detection Using DNS Traffic Analysis**

DNS Threat Detector is a defensive cybersecurity tool that analyzes DNS query behavior to identify **early indicators of compromise** such as malware beaconing, domain generation algorithms (DGA), DNS tunneling, and suspicious host activity  *before* payload delivery or data exfiltration occurs.

Unlike traditional DNS security tools that rely primarily on static blacklists or known malicious domains, this project focuses on **behavioral and anomaly-based detection**, making it effective against **unknown, zero-day, and newly registered attacker infrastructure**.

---

##  Why DNS?

DNS is one of the **earliest and most unavoidable steps** in most cyber attacks:
- Malware must resolve a domain before contacting command-and-control servers
- Phishing infrastructure relies on DNS before users ever see a page
- DNS traffic often bypasses stricter firewall controls

By monitoring DNS behavior, defenders gain **early visibility into attacks that have not fully executed yet**.

This tool is designed to act as an **early-warning system**, not just a post-incident detector.

---

##  What This Tool Detects

The system correlates multiple DNS-based signals to detect suspicious activity:

### 1. High-Entropy Domains  
Detects randomly generated or obfuscated domains often used in:
- DNS tunneling
- DGA-based malware

### 2. NXDOMAIN Abuse  
Identifies hosts repeatedly querying non-existent domains, a common trait of:
- Malware testing generated domains
- Failed C2 discovery attempts

### 3. Beaconing Behavior  
Flags repeated, patterned DNS queries that may indicate:
- Command-and-control communication
- Periodic malware check-ins

### 4. Abnormal Query Volume  
Detects internal hosts generating unusually high DNS traffic, which may suggest:
- Compromised endpoints
- Automated malware activity

### 5. AI-Based Anomaly Detection  
Uses unsupervised machine learning to learn **normal DNS behavior** and flag:
- Previously unseen or rule-evading patterns  
- Suspicious activity without relying on known signatures

---

##  What Makes This Project Different

Most DNS security tools:
- Depend heavily on known malicious domain lists
- Detect threats only after infrastructure is identified
- Produce alerts without investigation context

This project is different because it:
- Focuses on **behavior, not reputation**
- Detects **unknown and early-stage threats**
- Combines **multiple detection layers** instead of a single signal
- Provides **explainable results**, not black-box decisions
- Mirrors **real SOC workflows** with dashboards, risk scoring, and reports

It is designed to answer not just *“Is this malicious?”* but  
**“Why does this look suspicious, and what should be done next?”**

---

## 🏗️ Architecture Overview
```

DNS Logs (CSV)
↓
Statistical Detectors
(entropy, NXDOMAIN, beaconing, volume)
↓
AI Anomaly Detection
↓
Risk Scoring & Correlation
↓
Dashboards + SOC-Style PDF Report
```

Each detection layer strengthens confidence while reducing false positives.

---

## 📁 Project Structure


```
dns-threat-detector/
├── data/ # DNS log input
├── detectors/ # Rule-based detection modules
├── ai/ # ML-based anomaly detection
├── dashboard/ # Visual analytics
├── reports/ # PDF report generation
├── utils/ # Helper utilities
├── main.py # Orchestrator
├── requirements.txt
└── README.md
```


---

## ⚙️ Installation

### Prerequisites
- Python 3.9+
- Git

### Setup
```bash
git clone https://github.com/KDh3h3/dns-threat-detector.git
cd dns-threat-detector
pip install -r requirements.txt
```
Usage

Place DNS logs in data/dns_logs.csv
(or modify the path in main.py)

Run the tool:
```bash
python main.py
```



