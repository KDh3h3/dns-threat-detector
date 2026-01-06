def detect_nxdomain_abuse(logs, threshold=3):
    ip_counts = {}

    for log in logs:
        if log["response"] == "NXDOMAIN":
            ip_counts[log["src_ip"]] = ip_counts.get(log["src_ip"], 0) + 1

    return {ip: count for ip, count in ip_counts.items() if count >= threshold}
def detect_nxdomain_abuse(logs, threshold=3):
    ip_counts = {}

    for log in logs:
        if log["response"] == "NXDOMAIN":
            ip_counts[log["src_ip"]] = ip_counts.get(log["src_ip"], 0) + 1

    return {ip: count for ip, count in ip_counts.items() if count >= threshold}